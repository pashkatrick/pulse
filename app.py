from flask import Flask, Response, request, render_template
from core import task_manager, message_manager, prepare_manager
from decouple import config
import argparse

app = Flask(__name__, static_url_path='/static')
mm = message_manager.MessageManager()
prep = prepare_manager.PrepareManager()
tm = task_manager.TaskManager(mm)


@app.route('/')
def hello_world():
    # return dict(data='Welcome to Pulse')
    return render_template('index.html', config=prep.prepare_tiles())


@app.route('/start')
def start():
    # TODO: it doesn't work
    # conf = request.args.get('config')
    # theme = request.args.get('theme')
    # TODO: more exceptions and path validation via cmd
    # if conf or theme:
    #     prep.init_config(conf, theme)
    tm.init_cls(prep.prepare_cls())
    tm.start()
    return dict(data='started')


@app.route('/stop')
def stop():
    return tm.stop()


@app.route('/check')
def check():
    return tm.check()


@app.route('/listen', methods=['GET'])
def listen():

    def stream():
        messages = mm.consume()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg
    return Response(stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', action='store', default=config('PU_PORT'))    
    parser.add_argument('-a', '--address', action='store', default=config('PU_ADDRESS'))   
    parser.add_argument('-c', '--config', action='store', default=config('PU_CONFIG'))   
    parser.add_argument('-t', '--theme', action='store', default=config('PU_THEME'))   
    args = parser.parse_args()
    app.run(host=args.address, port=args.port, debug=config('PU_DEBUG'))
