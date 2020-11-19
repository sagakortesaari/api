import flask
from flask import request, jsonify
from connect import collection
import random

app = flask.Flask(__name__)

@app.route('/add', methods=["POST"])
def add():
    query = request.get_json()
    insert = request.get_json()
    collection.insert_one(query)
    return jsonify("successfully inserted!")

@app.route('/search/<type>')
def search(type):
    if (collection.find_one({"type": type}) != None):
        results = list(collection.find({"type": type}))
        print(results)
        return "<img src=" + random.choice(results)["url"] + ">"
    else:
        flask.abort(404)



