import requests
import httpx


def catcher(func):
    def wrapper(*args, **kwargs):
        wrap = func(*args, **kwargs)
        return wrap
    return wrapper


class HttpRaw():
    # def __new__(self, q):
    #     self.q = q

    def __init__(self, q):
        self.q = q

    def __str__(self):
        return f'im run with {self.q}'

    def __call__(self):
        print('i called')

    @catcher
    def request():
        pass

    def __available():
        pass

    def __add_cookies():
        pass

    def __data_extract():
        pass
