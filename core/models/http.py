import requests
from .base import Base


def catcher(func):
    def wrapper(*args, **kwargs):
        wrap = func(*args, **kwargs)
        return wrap
    return wrapper


class HttpStatus(Base):

    def __init__(self):
        self.tile_type = 'http_status'

    def request(self):
        response = requests.get('https://example.com/')
        return f'msg: from {__class__.__name__} with status: {response.status_code}'

    def __available():
        pass

    def __add_cookies():
        pass

    def __data_extract():
        pass
