from flask import Flask, Response
from core import task_manager, message_manager, prepare_manager

app = Flask(__name__)
mm = message_manager.MessageManager()
prep = prepare_manager.PrepareManager()
tm = task_manager.TaskManager(
    message_manager=mm, prepared_data=prep.prepare_cls())


@app.route('/')
def hello_world():
    return dict(data='Welcome to Pulse')


@app.route('/start')
def start():
    tm.start()
    return 'started'


@app.route('/stop')
def stop():
    return tm.stop()


@app.route('/check')
def check():
    return tm.check()


# TODO: delegate to FE
@app.route('/listen', methods=['GET'])
def listen():

    def stream():
        messages = mm.consume()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg

    return Response(stream(), mimetype='text/event-stream')
