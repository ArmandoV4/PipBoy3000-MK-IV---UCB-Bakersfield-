from resources.assets import Assets
from tabs.tab import Tab
from tabs.submenu import Submenu
from tabs.map.world_map import WorldMap

class MapTab(Tab):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name = 'MAP'
        self.submenus: list[Submenu] = [
            WorldMap(self.assets)
        ]
        self.subheader_surface = self.generate_subheader()