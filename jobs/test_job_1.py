
import this
from flask import Flask
from flask import request

app = Flask(__name__)

print('This is test job 1. Hihi')
a = 1 + 2
app.logger.warning('Tuyen testing warning log'+str(a))

message = 'Tuyen write a message: Hello from test_job_1.py'

def get_message():
    return message