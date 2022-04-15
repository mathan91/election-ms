import flask
import services.config.dbconnection as conn
import services.election.crud as service
from flask_pymongo import PyMongo

connection = conn.DBConnection()

app = flask.Flask(__name__)
mongo_uri = connection.getMyDb()
print(mongo_uri)
mongodb_client = PyMongo(app, uri=mongo_uri)
db = mongodb_client.db

@app.route("/add_one")
def add_one():
    if service.insertOne(db) == True:
        return flask.jsonify(message="success")
    else:
        return flask.jsonify(message="Failed to insert")

@app.route("/add_many")
def add_many():
    if service.insertMany(db) == True:
        return flask.jsonify(message="success")
    else:
        return flask.jsonify(message="Failed to insert")

@app.route("/delete_all")
def del_all():
    if service.deleteAll(db) == True:
        return flask.jsonify(message="Successfully Deleted")
    else:
        return flask.jsonify(message="Failed to delete")

@app.route("/")
def find():
    return service.findAll(db)

if __name__ == "__main__":
    app.run(debug=False, host = "0.0.0.0", port = 8081)