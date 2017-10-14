from flask import Blueprint, jsonify
from .controller import response

mod_emotion = Blueprint('mod_emotion', __name__, url_prefix='/emotion')


@mod_emotion.route('/')
def index():
    return jsonify(response)
