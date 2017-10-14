from flask import Flask
from .modules.index.controller import mod_index
from .modules.emotion import mod_emotion

app = Flask(__name__)

app.register_blueprint(mod_index)
app.register_blueprint(mod_emotion)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
