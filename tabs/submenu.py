import pygame
from collections.abc import Sized
from abc import ABC
from resources.assets import Assets
from utils.constants import (
    TOP_EDGE,
    RIGHT_EDGE,
    BOTTOM_EDGE,
    LEFT_EDGE,
    PIPBOY_GREEN,
    DIVIDER_X,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TAB,
    BLACK,
    MEDIUM,
    SMALL,
    DESC_TOP,
)

"""Contains an abstract class for each submenu and its universal methods.
"""


class Submenu(ABC):
    def __init__(self, assets: Assets) -> None:
        """Initializes universal class variables.

        Args:
            assets (Assets): passed through assets instance
        """
        self.assets: Assets = assets
        self.name: str = ""
        self.menu_index: int = 0
        self.scroll_offset: int = 0
        self.menu_index_changed = False
        self.working_area_edge: int = (
            TOP_EDGE
            + self.assets.fonts["large"].get_linesize()
            + self.assets.fonts["medium"].get_linesize()
        )
        self.width: int = RIGHT_EDGE - LEFT_EDGE
        self.height: int = BOTTOM_EDGE - self.working_area_edge

    def event_handler(self, event: pygame.event.Event) -> None:
        """Event handler method supposed to be implemented in all instances of a submenu

        Args:
            event (pygame.event.Event): passed through navigation events
        """
        pass

    def update(self, dt: float) -> None:
        """Update method supposed to be implemented in all instances of a submenu

        Args:
            dt (float): time between frames in seconds
        """
        pass
    
    def draw(self, screen: pygame.Surface) -> None:
        """Draw method meant to be implemented in all insances of a submenu

        Args:
            screen (pygame.Surface): target display surface
        """
        pass

    def scroll_down(self, items: Sized) -> None:
        """Method used to scroll down through the different items"""
        self.menu_index = (self.menu_index + 1) % len(items)
        self.menu_index_changed = True

    def scroll_up(self, items: Sized) -> None:
        """Method used to scroll up through the different items

        Args:
            items (Sized): _description_
        """
        self.menu_index = (self.menu_index - 1) % len(items)
        self.menu_index_changed = True

    def shift_image_hue(
        self, image: pygame.Surface, color: tuple[int, int, int]
    ) -> pygame.Surface:
        shifted = image.copy()
        tint = pygame.Surface(image.get_size()).convert_alpha()
        tint.fill(color)
        shifted.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return shifted

    def wrap_text(self, font: pygame.font.Font, text: str, max_width: int) -> list[str]:
        words: list[str] = text.split(" ")
        lines: list[str] = []
        current_line: str = ""

        for word in words:
            test_line: str = (current_line + " " + word).strip()
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    def draw_divider(self, surface: pygame.Surface) -> None:
        pygame.draw.line(
            surface,
            PIPBOY_GREEN,
            (DIVIDER_X, self.working_area_edge),
            (DIVIDER_X, BOTTOM_EDGE),
        )

    def update_scroll(self, total_items: int, line_spacing: int) -> None:
        max_visible: int = max(1, self.height // line_spacing)
        if self.menu_index < self.scroll_offset:
            self.scroll_offset = self.menu_index
        elif self.menu_index >= self.scroll_offset + max_visible:
            self.scroll_offset = self.menu_index - max_visible + 1

        max_offset = max(0, total_items - max_visible)
        self.scroll_offset = min(self.scroll_offset, max_offset)

    def generate_data_surface(self, data: list[dict[str, str]]) -> pygame.Surface:
        data_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        line_spacing: int = self.assets.fonts[MEDIUM].get_linesize()
        tab_size: int = self.assets.fonts[MEDIUM].size(TAB)[0]
        desc_line_height: int = self.assets.fonts[SMALL].get_linesize()
        desc_left = DIVIDER_X + tab_size
        right_panel_center_x = DIVIDER_X + (SCREEN_WIDTH - DIVIDER_X) // 2
        max_desc_width = SCREEN_WIDTH - desc_left - tab_size

        self.update_scroll(len(data), line_spacing)
        max_visible: int = max(1, self.height // line_spacing)
        visible_items = data[self.scroll_offset : self.scroll_offset + max_visible]

        for row, item in enumerate(visible_items):
            index = self.scroll_offset + row
            highlighted = index == self.menu_index

            name_surf = self.assets.fonts[MEDIUM].render(
                item.get("name", ""), True, BLACK if highlighted else PIPBOY_GREEN
            )
            name_rect = name_surf.get_rect(
                topleft=(LEFT_EDGE, self.working_area_edge + (row * line_spacing))
            )

            level_surf = self.assets.fonts[MEDIUM].render(
                item.get("level", ""), True, BLACK if highlighted else PIPBOY_GREEN
            )
            level_rect = level_surf.get_rect(
                topright=(DIVIDER_X, self.working_area_edge + (row * line_spacing))
            )

            highlight_rect = pygame.Rect(
                0,
                self.working_area_edge + row * line_spacing,
                DIVIDER_X,
                line_spacing,
            )

            if highlighted:
                item_img = self.assets.images.get(item.get("name", ""))
                if item_img:
                    item_img = self.shift_image_hue(item_img, PIPBOY_GREEN)
                    img_rect = item_img.get_rect(
                        center=(
                            right_panel_center_x,
                            (self.working_area_edge + DESC_TOP) // 2,
                        )
                    )
                    data_surf.blit(item_img, img_rect)
                desc_lines = self.wrap_text(
                    self.assets.fonts[SMALL], item.get("desc", ""), max_desc_width
                )

                for line_index, line in enumerate(desc_lines):
                    desc_surface = self.assets.fonts[SMALL].render(
                        line, True, PIPBOY_GREEN
                    )
                    desc_rect = desc_surface.get_rect(
                        topleft=(desc_left, DESC_TOP + line_index * desc_line_height)
                    )
                    data_surf.blit(desc_surface, desc_rect)

                pygame.draw.rect(data_surf, PIPBOY_GREEN, highlight_rect)

            data_surf.blit(name_surf, name_rect)
            data_surf.blit(level_surf, level_rect)

        pygame.draw.line(
            data_surf, PIPBOY_GREEN, (DIVIDER_X, DESC_TOP), (SCREEN_WIDTH, DESC_TOP)
        )
        self.draw_divider(data_surf)
        data_surf = data_surf.convert_alpha()
        return data_surf
