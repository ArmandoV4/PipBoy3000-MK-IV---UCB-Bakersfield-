import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.events import SCROLL_UP, SCROLL_DOWN
from utils.constants import ORIGIN

class Perks(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name = 'Perks'
        self.perks: list[dict[str, str]] =[
            {
                "name": "Confirmed Bachelor",
                "desc": "+10% damage to the same sex and unique dialogue options with certain characters. ",
            },
            {
                "name": "Educated",
                "desc": "You gain two more skill points every time you advance in level.",
            },
            {
                "name": "Bloody Mess",
                "desc": "+5% overall damage; more violent death animations. ",
            },
            {
                "name": "Good Natured",
                "desc": "Increases Speech, Medicine, Repair, Science and Barter skills +5. Decreases Energy Weapons, Explosives, Guns, Melee Weapons and Unarmed skills -5.",
            },
            {
                "name": "Wild Wasteland",
                "desc": "Adds additional 'wacky' content and modifies existing content and special encounters.",
            }
        ]
        self.perk_surface: pygame.Surface = self.generate_data_surface(self.perks)
    
    def event_handler(self, event: Event) -> None:
        if event.type == SCROLL_DOWN:
            self.scroll_down(self.perks)

        elif event.type == SCROLL_UP:
            self.scroll_up(self.perks)
    
    def update(self, dt: float) -> None:
        if self.menu_index_changed:
            self.perk_surface = self.generate_data_surface(self.perks)
            self.menu_index_changed = False

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.perk_surface, ORIGIN)