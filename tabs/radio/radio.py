import pygame
from resources.assets import Assets
from tabs.tab import Tab
from tabs.submenu import Submenu
from tabs.radio.radio_stations import RadioStation

class RadioTab(Tab):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name = 'RADIO'
        self.submenus: list[Submenu] = [
            RadioStation(self.assets),
        ]
        self.subheader_surfaces: dict[int, pygame.Surface] = {self.submenu_index : self.generate_subheader()}