import queue


class MessageManager:

    def __init__(self):
        self.listeners = []

    def consume(self):
        self.listeners.append(queue.Queue(maxsize=5))
        return self.listeners[-1]

    def produce(self, msg):
        # We go in reverse order because we might have to delete an element, which will shift the
        # indices backward
        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]
