from resources.assets import Assets
from tabs.tab import Tab
from tabs.submenu import Submenu
from tabs.inv.weapons import Weapons

class InventoryTab(Tab):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name: str = 'INV'
        self.submenus: list[Submenu] = [
            Weapons(self.assets)
        ]
        self.subheader_surface = self.generate_subheader()