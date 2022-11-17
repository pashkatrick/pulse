from random import randrange
from .base import Base


class Random(Base):
    def __init__(self):
        self.tile_type = 'random'

    def request(self):
        return randrange(100)
