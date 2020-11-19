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


