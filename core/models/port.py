from .base import Base
import socket


class Port(Base):
    def __init__(self):
        self.tile_type = 'port'

    def request(self):
        response = ''
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # TODO: test & fix that
        result = sock.connect_ex(('127.0.0.1', 80))
        response = 'open' if result == 0 else 'not open'
        sock.close()
        return response
