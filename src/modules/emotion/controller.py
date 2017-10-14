from flask import Blueprint

mod_emotion = Blueprint('mod_emotion', __name__, url_prefix='/emotion')


@mod_emotion.route('/')
def index():
    return 'Hello Emotion!'
