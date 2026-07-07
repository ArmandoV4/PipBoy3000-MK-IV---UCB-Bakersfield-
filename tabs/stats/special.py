import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.constants import (
    ORIGIN,
)
from utils.events import SCROLL_UP, SCROLL_DOWN


class Special(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name: str = "SPECIAL"
        self.stats: list[dict[str, str]] = [
            {
                "name": "Strength",
                "level": "5",
                "desc": "Strength is a measure of your raw physical power. It affects how much you can carry and the damage of all melee attacks.",
            },
            {
                "name": "Perception",
                "level": "5",
                "desc": "Perception is your environmental awareness and 'sixth sense,' and affects weapon accuracy in V.A.T.S.",
            },
            {
                "name": "Endurance",
                "level": "5",
                "desc": "Endurance is the measure of your physical fitness. It affects your total Health and the action point drain from sprinting.",
            },
            {
                "name": "Charisma",
                "level": "5",
                "desc": "Charisma is the ability to charm and convice others. It affects your chance to persuade in dialogue and prices when you barter.",
            },
            {
                "name": "Intelligence",
                "level": "5",
                "desc": "Intelligence is a measure of your overall mental acuity, and affects the number of Experience Points earned.",
            },
            {
                "name": "Agility",
                "level": "5",
                "desc": "Agility is the measurement of your overall fitness and reflexes. It affects the number of Action Points in V.A.T.S. and your ability to sneak.",
            },
            {
                "name": "Luck",
                "level": "5",
                "desc": "Luck is a measurement of your general good fortune, and affects the recharge rate of Critical Hits.",
            },
        ]
        self.special_surface: pygame.Surface = self.generate_data_surface(self.stats)

    def event_handler(self, event: Event) -> None:
        if event.type == SCROLL_DOWN:
            self.scroll_down(self.stats)

        elif event.type == SCROLL_UP:
            self.scroll_up(self.stats)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.special_surface, ORIGIN)

    def update(self, dt: float) -> None:
        if self.menu_index_changed:
            self.special_surface = self.generate_data_surface(self.stats)
            self.menu_index_changed = False
