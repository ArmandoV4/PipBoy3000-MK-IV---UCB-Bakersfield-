import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.constants import (
    LEFT_EDGE, 
    PIPBOY_GREEN,
    BLACK, 
    SMALL,
    MEDIUM,
    DIVIDER_X,
    DESC_TOP, 
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ORIGIN, 
    TAB
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
        self.special_surface: pygame.Surface = self.generate_special_surface()

    def event_handler(self, event: Event) -> None:
        if event.type == SCROLL_DOWN:
            self.scroll_down(self.stats)

        elif event.type == SCROLL_UP:
            self.scroll_up(self.stats)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.special_surface, ORIGIN)

    def update(self, dt: float) -> None:
        if self.menu_index_changed:
            self.special_surface = self.generate_special_surface()
            self.menu_index_changed = False

    def generate_special_surface(self) -> pygame.Surface:
        special_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

        # Calculate spacing and sizes
        line_spacing: int = self.assets.fonts[MEDIUM].get_linesize()
        tab_size: int = self.assets.fonts[MEDIUM].size(TAB)[0]
        desc_line_height: int = self.assets.fonts[SMALL].get_linesize()
        desc_left = DIVIDER_X + tab_size
        right_panel_center_x = DIVIDER_X + (SCREEN_WIDTH - DIVIDER_X) // 2
        max_desc_width = SCREEN_WIDTH - desc_left - tab_size
        
        for index, stat in enumerate(self.stats):
            highlighted = index == self.menu_index
            top_edge = self.working_area_edge + (index * line_spacing)

            name_surf = self.assets.fonts[MEDIUM].render(stat['name'], True, BLACK if highlighted else PIPBOY_GREEN)
            name_rect = name_surf.get_rect(topleft = (LEFT_EDGE, top_edge))

            level_surf = self.assets.fonts[MEDIUM].render(stat['level'], True, BLACK if highlighted else PIPBOY_GREEN)
            level_rect = level_surf.get_rect(topright = (DIVIDER_X, self.working_area_edge + (index * line_spacing)))
            
            highlight_rect = name_rect.union(level_rect)

            if highlighted:
                stat_image = self.shift_image_hue(self.assets.special_images[stat['name']], PIPBOY_GREEN)
                desc_lines = self.wrap_text(self.assets.fonts[SMALL], stat['desc'], max_desc_width)
                desc_top = DESC_TOP
                stat_image_rect = stat_image.get_rect(center=(right_panel_center_x, (self.working_area_edge + desc_top) // 2))

                for line_index, line in enumerate(desc_lines):
                    desc_surface = self.assets.fonts[SMALL].render(line, True, PIPBOY_GREEN)
                    desc_rect = desc_surface.get_rect(topleft=(desc_left, desc_top + line_index * desc_line_height))
                    special_surf.blit(desc_surface, desc_rect)

                pygame.draw.rect(special_surf, PIPBOY_GREEN, highlight_rect)
                pygame.draw.line(special_surf, PIPBOY_GREEN, (DIVIDER_X, desc_top), (SCREEN_WIDTH, desc_top))
                special_surf.blit(stat_image, stat_image_rect)

            special_surf.blit(name_surf, name_rect)
            special_surf.blit(level_surf, level_rect)
            self.draw_divider(special_surf)
            special_surf.convert_alpha()

        return special_surf