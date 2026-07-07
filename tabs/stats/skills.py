import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.events import SCROLL_UP, SCROLL_DOWN
from utils.constants import ORIGIN


class Skills(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name = "Skills"
        self.skills: list[dict[str, str]] = [
            {
                "name": "Barter",
                "desc": "Proficiency at trading and haggling. Also used to negotiate better quest rewards or occasionally as a bribe-like alternative to Speech.",
                "level": "50",
            },
            {
                "name": "Energy Weapons",
                "desc": "Proficiency at using energy-based weapons. ",
                "level": "50",
            },
            {
                "name": "Explosives",
                "desc": "Proficiency at using explosive weaponry, disarming mines, and crafting explosives.",
                "level": "50",
            },
            {
                "name": "Guns",
                "desc": "Proficiency at using weapons that fire standard ammunition.",
                "level": "50",
            },
            {
                "name": "Lockpick",
                "desc": "Proficiency at picking locks.",
                "level": "50",
            },
            {
                "name": "Medicine",
                "desc": "Proficiency at using medical tools, drugs, and for crafting Doctor's Bags.",
                "level": "50",
            },
            {
                "name": "Melee Weapons",
                "desc": "Proficiency at using melee weapons.",
                "level": "50",
            },
            {
                "name": "Repair",
                "desc": "Proficiency at repairing items and crafting items and ammunition.",
                "level": "50",
            },
            {
                "name": "Science",
                "desc": "Proficiency at hacking terminals, recycling energy ammunition at workbenches, crafting chems, and many dialog checks.",
                "level": "50",
            },
            {
                "name": "Sneak",
                "desc": "Proficiency at remaining undetected and stealing.",
                "level": "50",
            },
            {
                "name": "Speech",
                "desc": "Proficiency at persuading others. Used to negotiate for better quest rewards, talk your way out of combat, and convince people to give up vital information.",
                "level": "50",
            },
            {
                "name": "Survival",
                "desc": "Proficiency at cooking, making poisons, and crafting 'natural' equipment and consumables. Also yields increased benefits from food.",
                "level": "50",
            },
            {
                "name": "Unarmed",
                "desc": "Proficiency at unarmed fighting. ",
                "level": "50",
            },
        ]
        self.skill_surface: pygame.Surface = self.generate_data_surface(self.skills)

    def event_handler(self, event: Event) -> None:
        if event.type == SCROLL_DOWN:
            self.scroll_down(self.skills)

        elif event.type == SCROLL_UP:
            self.scroll_up(self.skills)

    def update(self, dt: float) -> None:
        if self.menu_index_changed:
            self.skill_surface = self.generate_data_surface(self.skills)
            self.menu_index_changed = False
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.skill_surface, ORIGIN)
