from flask import Blueprint, jsonify
from flask_cors import cross_origin
from .controller import response

mod_emotion = Blueprint('mod_emotion', __name__, url_prefix='/emotion')


@mod_emotion.route('/')
@cross_origin()
def index():
    return jsonify(response)
