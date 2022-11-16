from .base import Base
from pythonping import ping

# sudo required
class Ping(Base):
    def __init__(self):
        self.tile_type = 'ping'
        # host - require
        # size - optional
        # count - optional

    def request(self):
        response_list = ping('8.8.8.8', size=10, count=2)
        return f'{response_list.rtt_avg_ms} ms'
