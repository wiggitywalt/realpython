#blog.py - controller

#imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
from functools import wraps

import sqlite3

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'UV\xf4\x0c\xce\xb0\xf6\xa6\xa1\xbf-\x02\x9c\xb3\xc7\xf1< oz\x0f\xb5\x99\x1e'
#SECRET_KEY = 'laserjorples'

app = Flask(__name__)

#pulls in app configuration by looking for UPPDERCASE variables
app.config.from_object(__name__)

#function used for connecting to database

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap


@app.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']
    post = request.form['post']
    if not title or not post:
        flash("All fields are required! Damn! Try again!")
        return redirect(url_for('main'))
    else:
        g.db = connect_db()
        g.db.execute('insert into posts(title,post) VALUES(?,?)', [request.form['title'], request.form['post']])
        g.db.commit()
        g.db.close()
        flash('New entry was saved')
        return redirect(url_for('main'))
@app.route('/main')
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html',posts=posts)

if __name__ == '__main__':
    app.run(debug=True)



























