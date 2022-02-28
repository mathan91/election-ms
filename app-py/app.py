import flask
from flask import render_template
from flask_pymongo import PyMongo
import config.dbconnection as conn

connection = conn.DBConnection()

app = flask.Flask(__name__)
mongo_uri = connection.getMyDb("my-db")
print(mongo_uri)
mongodb_client = PyMongo(app, uri=mongo_uri)
db = mongodb_client.db

@app.route("/add_one")
def add_one():
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")

@app.route("/add_many")
def add_many():
    db.todos.insert_many([
        {'_id': 11, 'title': "todo title one ", 'body': "todo body one "},
        {'_id': 22, 'title': "todo title two", 'body': "todo body two"},
        {'_id': 33, 'title': "todo title three", 'body': "todo body three"},
        {'_id': 44, 'title': "todo title four", 'body': "todo body four"},
        {'_id': 55, 'title': "todo title five", 'body': "todo body five"},
        {'_id': 15, 'title': "todo title six", 'body': "todo body six"},
        ])
    return flask.jsonify(message="success")

@app.route("/delete_all")
def del_all():
    for todo in db.todos.find():
        db.todos.delete_one(todo)
    return flask.jsonify(message="success")

@app.route("/")
def index():
    todos = db.todos.find()
    return flask.jsonify([todo for todo in todos])

if __name__ == "__main__":
    app.run(debug=False, host = "0.0.0.0")