from flask import Flask
from src.modules.index import mod_index
from src.modules.emotion import mod_emotion

app = Flask(__name__)

app.register_blueprint(mod_index)
app.register_blueprint(mod_emotion)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
