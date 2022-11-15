from random import randrange
from .base import Base


class Ping(Base):
    def __init__(self):
        self.tile_type = 'ping'

    def request(self):
        return randrange(100)
