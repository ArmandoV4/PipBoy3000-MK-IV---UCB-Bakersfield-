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
    DESC_TOP,
    SMALL,
)

from widgets.widget import Widget
from widgets.menu_selector import MenuSelector
from widgets.description_panel import DescriptionPanel
from widgets.image_panel import ImagePanel

class Skills(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name = "Skills"
        self.data: list[dict[str, str]] = [
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
        self.menu_selector = MenuSelector(
            pygame.Rect(
                0,
                self.working_area_edge,
                DIVIDER_X,
                BOTTOM_EDGE - self.working_area_edge,
            ),
            assets,
            self.generate_labels(),
            self.generate_levels(),
            MEDIUM,
            PIPBOY_GREEN,
            BLACK,
        )

        self.description_panel = DescriptionPanel(
            pygame.Rect(
                DIVIDER_X, DESC_TOP, SCREEN_WIDTH - DIVIDER_X, BOTTOM_EDGE - DESC_TOP
            ),
            self.assets,
            self.data[self.menu_selector.get_selected_index()].get("desc", ""),
            SMALL,
            PIPBOY_GREEN,
        )
        self.image_panel = ImagePanel(
            pygame.Rect(
                DIVIDER_X,
                self.working_area_edge,
                SCREEN_WIDTH - DIVIDER_X,
                DESC_TOP - self.working_area_edge,
            ),
            self.assets,
            self.data[self.menu_selector.get_selected_index()].get("name", ""),
            PIPBOY_GREEN,
        )
        self.widgets: list[Widget] = [
            self.menu_selector,
            self.description_panel,
            self.image_panel,
        ]
        self.special_surface: pygame.Surface = self.generate_surf()

    def event_handler(self, event: Event) -> None:
        self.menu_selector.event_handler(event)

    def update(self, dt: float) -> None:
        surface_changed = False
        if self.menu_selector.changed:
            self.sync_description()
            self.sync_image_path()
            surface_changed = True

        for widget in self.widgets:
            widget.update(dt)

        if surface_changed:
            self.special_surface = self.generate_surf()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.special_surface, ORIGIN)

    def generate_labels(self) -> list[str]:
        return [item.get("name", "") for item in self.data]

    def generate_levels(self) -> list[str]:
        return [item.get("level", "") for item in self.data]

    def generate_surf(self) -> pygame.Surface:
        surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        for widget in self.widgets:
            surf.blit(widget.surf, widget.rect.topleft)
            pygame.draw.rect(surf, PIPBOY_GREEN, widget.rect, 1)
        return surf

    def sync_description(self) -> None:
        selected_index = self.menu_selector.get_selected_index()
        self.description_panel.set_desc(self.data[selected_index].get("desc", ""))

    def sync_image_path(self) -> None:
        selected_index = self.menu_selector.get_selected_index()
        self.image_panel.set_image_key(self.data[selected_index].get("name", ""))
