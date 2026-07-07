import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.events import SCROLL_UP, SCROLL_DOWN

class Perks(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name = 'Perks'