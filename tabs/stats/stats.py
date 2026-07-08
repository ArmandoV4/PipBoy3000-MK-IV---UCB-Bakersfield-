import pygame
from resources.assets import Assets
from tabs.tab import Tab
from tabs.submenu import Submenu
from tabs.stats.status import Status
from tabs.stats.special import Special
from tabs.stats.skills import Skills
from tabs.stats.perks import Perks


""" Contains the Stats tab and its associated submenus
"""

class StatsTab(Tab):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name: str = 'STATS'
        self.submenus: list[Submenu] = [
            Status(self.assets),
            Special(self.assets),
            Skills(self.assets),
            Perks(self.assets),
            ]
        self.subheader_surfaces: dict[int, pygame.Surface] = {self.submenu_index : self.generate_subheader()}