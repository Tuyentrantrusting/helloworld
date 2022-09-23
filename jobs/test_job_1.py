import logging

print('This is test job 1. Hihi')
message = 'Tuyen write a message: Hello from test_job_1.py'
def get_message():
    return message


logging.warning("This is a warning!")
raise NotImplementedError(f"An example error")