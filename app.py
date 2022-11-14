from flask import Flask
from core import task_manager

app = Flask(__name__)
tm = task_manager.TaskMaster()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/start')
def start():
    tm.start()
    return 'started'


@app.route('/stop')
def stop():
    tm.stop()
    return 'stoped'


@app.route('/check')
def check():
    tm.check()
    return 'checked'
