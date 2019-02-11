from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    data={}
    data["saludo"]="Hello World"
    return jsonify(data)

if __name__ == "__main__":
    app.run()


def create_app():
    return app

