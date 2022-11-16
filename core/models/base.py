from .schema import TileResponse, TypeEnum


class Base():
    def __call__(self):
        response = TileResponse(
            type=TypeEnum[self.tile_type].value, response=self.request())
        return response.dict()
