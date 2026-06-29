from resources.assets import Assets
from tabs.submenu import Submenu

class WorldMap(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name: str = 'WORLD MAP'