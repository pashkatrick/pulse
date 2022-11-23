from .models import schemes
from decouple import config


class PrepareManager():

    def __init__(self):
        self.config_path = config('PU_CONFIG')
        self.theme_path = config('PU_THEME')

    def read_config(self):
        scheme = schemes.ConfigSchema.parse_file(self.config_path)
        return scheme.tiles

    def prepare_cls(self) -> list:
        tiles = self.read_config()
        cls_list = []
        for tile in tiles:
            module_name, class_name = self._convert(tile.type.value)
            module = __import__('core.models', globals(), locals(), [module_name], 0)
            class_ = getattr(module, class_name)
            instance = class_()
            cls_list.append(instance)
        return cls_list

    def _convert(self, tile_name: str):
        if '-' in tile_name:
            module_name = tile_name.lower().replace('-', '_')
            class_name = module_name.replace('_', ' ').title().replace(' ', '')
        else:
            module_name = tile_name.lower()
            class_name = module_name.capitalize()
        return module_name, class_name

    def init_config(self, conf, theme):
        self.config_path = conf
        self.theme_path = theme
