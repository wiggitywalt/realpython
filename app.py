from flask import Flask

app = Flask(__name__)

app.config["DEBUG"]=True

@app.route("/name/<name>")
def index(name):
  if name.lower() == "michael":
    return "hello, {}".format(name), 200
  else:
    return "Not found", 404

@app.route("/test/<search_query>")
def search(search_query):
  return search_query

@app.route("/")
def hello_world():
  return "Hello, World!>!>!>??!"

@app.route("/hello")
def howdy():
  return "Howdy!"

if __name__ == "__main__":
  app.run()
