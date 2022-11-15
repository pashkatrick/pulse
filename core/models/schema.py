from pydantic import BaseModel as bm
from enum import Enum


class TypeEnum(str, Enum):
    random = 'RANDOM'
    ping = 'PING'
    port = 'PORT'
    http_status = 'HTTP-STATUS'


class TileResponse(bm):
    type: TypeEnum
    response: int | str

    class Config:
        use_enum_values = True


class Params(bm):
    pass


class Tile(bm):
    type: TypeEnum | None
    label: str
    params: Params | None


class ConfigSchema(bm):
    version: str
    columns: int
    tiles: list[Tile]
