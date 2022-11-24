from threading import Thread
from time import sleep
from decouple import config
import json

TIMEOUT = config('PU_TIMEOUT', default=5)


class TaskManager():

    def __init__(self, message_manager):
        self._running = True
        self._sse = message_manager
        self._cls = []
        self.thread = ''

    def start(self):
        self._running = True
        self.thread = Thread(target=self.run, daemon=True, name='infinity')
        self.thread.start()

    def stop(self):
        self._running = False
        self.thread.join()
        return dict(data='stopped')

    def run(self):
        # TODO: move it from task_manager at all
        def format_sse(data, event=None) -> str:
            _msg = f'data: {data}\n\n'
            if event is not None:
                _msg = f'event: {event}\n{_msg}'
            return _msg

        sse = self._sse
        while self._running:
            sleep(int(TIMEOUT))
            for i, cls in enumerate(self._cls):
                # we can add i to class init as tile ID
                msg = cls.__call__(i)
                # print to cli | optional
                # print(msg)
                f_msg = format_sse(data=json.dumps(msg), event='message')
                print(f_msg)
                sse.produce(msg=f_msg)

    def check(self):
        return dict(data='running') if self._running else dict(data='not running')

    def init_cls(self, prepared_data):
        self._cls = prepared_data
