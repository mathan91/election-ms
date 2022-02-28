import services.config.dbconnection  as connection
import flask

def findAll(db):
    todos = db.todos.find()
    return flask.jsonify([todo for todo in todos])

def deleteAll(db):
    for todo in db.todos.find():
        db.todos.delete_one(todo)
    return True

def insertMany(db):
    db.todos.insert_many([
        {'_id': 11, 'title': "todo title one ", 'body': "todo body one "},
        {'_id': 22, 'title': "todo title two", 'body': "todo body two"},
        {'_id': 33, 'title': "todo title three", 'body': "todo body three"},
        {'_id': 44, 'title': "todo title four", 'body': "todo body four"},
        {'_id': 55, 'title': "todo title five", 'body': "todo body five"},
        {'_id': 15, 'title': "todo title six", 'body': "todo body six"},
        ])
    return True

def insertOne(db):
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return True
