from random import randrange
from .base import Base


class Port(Base):
    def __init__(self):
        self.tile_type = 'port'

    def request(self):
        return randrange(100)
