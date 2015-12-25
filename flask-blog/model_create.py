import sqlite3

with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE posts (title TEXT, post TEXT) ")
    c.execute('insert into posts values("GOOD", "I am good.")')
    c.execute('insert into posts values("WELL!", "I am are well")')
    c.execute('insert into posts values("Excelllent", "yep. I am excellent")')
    c.execute('insert into posts values("ok", "I am just okay today")')

print "done"
