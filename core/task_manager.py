from threading import Thread
from time import sleep
import json


class TaskManager():

    def __init__(self, message_manager):
        self._running = True
        self._sse = message_manager
        self._cls = []

    def start(self):
        self._running = True
        # TODO: duplicate thread issue
        t = Thread(target=self.run, daemon=True, name='infinity')
        t.start()

    def stop(self):
        self._running = False
        return dict(data='stopped')

    def run(self):
        # TODO: move it from task_manager at all
        sse = self._sse
        while self._running:
            sleep(2)
            for i, cls in enumerate(self._cls):
                # we can add i to class init as tile ID
                test = cls.__call__(i)
                # print to cli | optional
                print(test)
                # print to web | optional
                js = json.dumps(test).encode('utf-8')
                sse.produce(msg=js)

    def check(self):
        return dict(data='running') if self._running else dict(data='not running')

    def init_cls(self, prepared_data):
        self._cls = prepared_data
