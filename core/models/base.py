from .schemes import TileResponse, TypeEnum


class Base():
    def __call__(self, _id):
        response = TileResponse(
            id=_id, type=TypeEnum[self.tile_type].value, response=self.request())
        return response.dict()
