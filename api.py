import flask
from flask import request, jsonify
from connect import collection

app = flask.Flask(__name__)

@app.route('/api/add/<word>')
def add(word):
    if (collection.find_one({"word" : word}) == None):
        obj = {
            "word": word
        }
        collection.insert_one(obj)
        return jsonify(word, "successfully added!")
    else:
        flask.abort(404)

@app.route('/api/search/<word>')
def search(word):
    if (collection.find_one({"word": word}) != None):
        return jsonify(word, "found!")
    else:
        flask.abort(404)
