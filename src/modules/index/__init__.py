from flask import Blueprint, jsonify
from flask_cors import cross_origin
from .controller import response

mod_index = Blueprint('mod_index', __name__)


@mod_index.route('/')
@cross_origin()
def index():
    return jsonify(response)
