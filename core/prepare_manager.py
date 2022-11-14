from . import schema

class PrepareManager():

    def __init__(self):
        self.scheme = schema.ConfigSchema()
        pass

    def read_config(self):
        pass