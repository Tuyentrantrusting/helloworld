import os

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    username = request.args.get('username')
    password = request.args.get('password')
    return "Hello {}! Your username is {}".format(name, username)
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
