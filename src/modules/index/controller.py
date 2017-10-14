from flask import Blueprint

mod_index = Blueprint('mod_index', __name__)


@mod_index.route('/')
def index():
    return 'Hello World!'
