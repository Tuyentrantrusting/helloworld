import os
from re import template
from flask import Flask, request, render_template
import importlib
#from jobs.test_ping import simple_ping

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    username = request.args.get('username')
    password = request.args.get('password')
    #hungcreds = os.environ.get("hunggmail")
    #return "Hello {}! Your username is {}".format(name, username)
    return render_template('index.html')
    
@app.route('/runjob', methods=['GET', 'POST'])
def runjob():
    jobname = request.args.get('jobname')
    job_module = importlib.import_module('jobs.'+jobname)
    message = job_module.get_message()
    return render_template('index.html', jobname=jobname, job_message=message)

@app.route('/printlog')
def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Printed log. Check your console"
    




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    

# %%
