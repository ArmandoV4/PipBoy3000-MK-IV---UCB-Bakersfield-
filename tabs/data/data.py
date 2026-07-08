import pygame
from resources.assets import Assets
from tabs.tab import Tab
from tabs.submenu import Submenu
from tabs.data.quests import Quests

class DataTab(Tab):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name: str = 'DATA'
        self.submenus: list[Submenu] = [
            Quests(self.assets)
        ]
        self.subheader_surfaces: dict[int, pygame.Surface] = {self.submenu_index : self.generate_subheader()}