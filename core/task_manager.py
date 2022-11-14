from threading import Thread
from time import sleep


class TaskMaster():

    def __init__(self):
        self._running = True

    def start(self):
        self.prepare()
        self._running = True
        t = Thread(target=self.run, daemon=True, name='Infinity')
        t.start()

    def prepare(self):
        pass

    def stop(self):
        self._running = False

    def check(self):
        if self._running:
            return 'Still running'
        else:
            return 'Stoped/Completed'

    def run(self):
        while self._running:
            sleep(2)
            print('kek')
