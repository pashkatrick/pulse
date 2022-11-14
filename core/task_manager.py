from threading import Thread
from time import sleep
from .models import http, random


class TaskManager():

    def __init__(self, message_manager):
        self._running = True
        self._sse = message_manager

    def start(self):
        self._running = True
        # TODO: duplicate thread issue
        t = Thread(target=self.run, daemon=True, name='Infinity')
        t.start()

    def stop(self):
        self._running = False

    def run(self):
        sse = self._sse
        cls_list = self.prepare()
        while self._running:
            sleep(2)
            for cls in cls_list:
                sse.produce(msg=cls.__call__())

    # TODO: separate of course
    def prepare(self) -> list:
        a = http.HttpRaw()
        b = random.Random()
        return [a, b]

    def check(self):
        if self._running:
            return 'Still running'
        else:
            return 'Stoped/Completed'
