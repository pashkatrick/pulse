from threading import Thread
from time import sleep
import json


class TaskManager():

    def __init__(self, message_manager, prepared_data: list):
        self._running = True
        self._sse = message_manager
        self._cls = prepared_data

    def start(self):
        self._running = True
        # TODO: duplicate thread issue
        t = Thread(target=self.run, daemon=True, name='infinity')
        t.start()

    def stop(self):
        self._running = False
        return dict(data='stopped')

    def run(self):
        sse = self._sse
        while self._running:
            sleep(2)
            for cls in self._cls:
                test = cls.__call__()
                print(test)
                # print to web | optional
                js = json.dumps(test).encode('utf-8')
                sse.produce(msg=js)

    def check(self):
        return dict(data='running') if self._running else dict(data='not running')
