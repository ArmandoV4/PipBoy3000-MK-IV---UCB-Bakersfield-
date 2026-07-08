from resources.assets import Assets
from application.managers import Managers
from tabs.tab import Tab
from tabs.submenu import Submenu
from tabs.map.world_map import WorldMap

class MapTab(Tab):
    def __init__(self, assets: Assets, managers: Managers) -> None:
        super().__init__(assets)
        self.name = 'MAP'
        self.submenus: list[Submenu] = [
            WorldMap(self.assets, managers.gps_manager)
        ]
        self.subheader_surface = self.generate_subheader()