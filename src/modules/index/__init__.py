from flask import Blueprint, jsonify
from .controller import response

mod_index = Blueprint('mod_index', __name__)


@mod_index.route('/')
def index():
    return jsonify(response)
