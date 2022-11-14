from random import randrange


def catcher(func):
    def wrapper(*args, **kwargs):
        wrap = func(*args, **kwargs)
        return wrap
    return wrapper


class Random():
    # def __new__(self, q):
    #     self.q = q

    def __init__(self):
        pass

    def __str__(self):
        pass

    def __call__(self):
        # print(f'msg: from {__class__.__name__} with data: {randrange(100)}')
        return f'msg: from {__class__.__name__} with data: {randrange(100)}\n'

    @catcher
    def request():
        pass

    def __available():
        pass

    def __add_cookies():
        pass

    def __data_extract():
        pass
