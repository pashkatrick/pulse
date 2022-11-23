from pydantic import BaseModel as bm
from pydantic import Field
from enum import Enum


class TypeEnum(str, Enum):
    random = 'RANDOM'
    ping = 'PING'
    port = 'PORT'
    http_status = 'HTTP-STATUS'


class StatusEnum(str, Enum):
    green = 'green'
    yellow = 'yellow'
    red = 'red'


class TileResponse(bm):
    id: int | None
    type: TypeEnum
    status: StatusEnum | None
    response: int | str

    class Config:
        use_enum_values = True


class Params(bm):
    pass


class Alert(bm):
    pass


class Tile(bm):
    # id: int = Field(primary_key=True)
    type: TypeEnum | None
    label: str
    params: Params | None
    alert: Alert | None


class ConfigSchema(bm):
    version: str
    columns: int
    tiles: list[Tile]
