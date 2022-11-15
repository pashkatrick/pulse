from .models import schema, http, random, ping, port


class PrepareManager():

    def __init__(self):
        # self.scheme = schema.ConfigSchema()
        pass

    def read_config(self):
        pass

    def prepare(self) -> list:
        a = http.HttpRaw()
        b = random.Random()
        c = ping.Ping()
        d = port.Port()
        return [a, b, c, d]
