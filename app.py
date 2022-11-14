from flask import Flask, Response
from core import task_manager, message_manager

app = Flask(__name__)
mm = message_manager.MessageManager()
tm = task_manager.TaskManager(message_manager=mm)


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

# TODO: delegate to FE
@app.route('/listen', methods=['GET'])
def listen():

    def stream():
        messages = mm.consume()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg

    return Response(stream(), mimetype='text/event-stream')
