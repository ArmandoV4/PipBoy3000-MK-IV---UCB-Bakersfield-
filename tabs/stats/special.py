import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.constants import (
    ORIGIN,
    PIPBOY_GREEN,
    BLACK,
    MEDIUM,
    DIVIDER_X,
    BOTTOM_EDGE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from widgets.widget import Widget
from widgets.menu_selector import MenuSelector


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
        self.widgets: list[Widget] = [
            MenuSelector(
                pygame.Rect(
                    0,
                    self.working_area_edge,
                    DIVIDER_X,
                    BOTTOM_EDGE - self.working_area_edge,
                ),
                assets,
                self.generate_labels(),
                self.generate_levels(),
                self.menu_index,
                MEDIUM,
                PIPBOY_GREEN,
                BLACK,
            )
        ]
        self.special_surface: pygame.Surface = self.generate_surf()

    def event_handler(self, event: Event) -> None:
        for widget in self.widgets:
            widget.event_handler(event)

    def update(self, dt: float) -> None:
        surface_changed = False

        for widget in self.widgets:
            was_changed = widget.changed
            widget.update(dt)

            if was_changed:
                surface_changed = True

        if surface_changed:
            self.special_surface = self.generate_surf()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.special_surface, ORIGIN)

    def generate_labels(self) -> list[str]:
        return [item.get("name", "") for item in self.stats]

    def generate_levels(self) -> list[str]:
        return [item.get("level", "") for item in self.stats]

    def generate_surf(self) -> pygame.Surface:
        surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        for widget in self.widgets:
            surf.blit(widget.surf, widget.rect.topleft)
        return surf
