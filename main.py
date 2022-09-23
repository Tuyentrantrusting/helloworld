import os

from flask import Flask
from flask import request
from jobs import 

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    username = request.args.get('username')
    password = request.args.get('password')
    hungcreds = os.environ.get("hunggmail")
    return "Hello {}! Your username is {}. Hung Creds is {}".format(name, username,hungcreds)
    
@app.route('/runjob', methods=['GET', 'POST'])
def runjob():
    jobname = request.args.get('jobname')
    return "Running job" + jobname
    




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
