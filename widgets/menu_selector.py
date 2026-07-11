import pygame
from pygame.event import Event
from resources.assets import Assets
from widgets.widget import Widget
from utils.constants import TAB
from utils.events import SCROLL_DOWN, SCROLL_UP


class MenuSelector(Widget):
    def __init__(
        self,
        rect: pygame.Rect,
        assets: Assets,
        labels: list[str],
        levels: list[str] | None,
        font_key: str,
        text_color: tuple[int, int, int],
        highlight_text_color: tuple[int, int, int]
    ) -> None:
        super().__init__(rect, assets)
        self.labels = labels
        self.levels = levels
        if levels is not None and len(labels) != len(levels):
            raise ValueError("length of levels and labels must match")
        self.index: int = 0
        self.font_key = font_key
        self.text_color = text_color
        self.highlight_text_color = highlight_text_color
        self.line_spacing: int = self.assets.fonts[font_key].get_linesize()
        self.indent_size: int = self.assets.fonts[font_key].size(TAB)[0]
        self.max_visible: int = max(1, self.rect.height // self.line_spacing)
        self.scroll_offset: int = 0
        self.surf = self.generate_surf()

    def event_handler(self, event: Event) -> None:
        if event.type == SCROLL_DOWN:
            self.scroll_down()

        elif event.type == SCROLL_UP:
            self.scroll_up()

    def update(self, dt: float) -> None:
        if self.changed:
            self.update_scroll()
            self.surf = self.generate_surf()
            self.changed = False

    def generate_surf(self) -> pygame.Surface:
        selector_surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        visible_items = self.labels[
            self.scroll_offset : self.scroll_offset + self.max_visible
        ]
        for row, label in enumerate(visible_items):
            index = self.scroll_offset + row
            highlighted = index == self.index
            if highlighted:
                highlight_rect = pygame.Rect(
                    0, row * self.line_spacing, self.rect.width, self.line_spacing
                )

                pygame.draw.rect(selector_surf, self.text_color, highlight_rect)

            if self.levels is not None:
                level_surf = self.assets.fonts[self.font_key].render(
                    self.levels[index],
                    True,
                    self.highlight_text_color if highlighted else self.text_color,
                )
                level_rect = level_surf.get_rect(
                    topright=(
                        self.rect.width,
                        row * self.line_spacing,
                    )
                )
                selector_surf.blit(level_surf, level_rect)

            label_surf = self.assets.fonts[self.font_key].render(
                label,
                True,
                self.highlight_text_color if highlighted else self.text_color,
            )

            label_rect = label_surf.get_rect(
                topleft=(self.indent_size, (row * self.line_spacing))
            )

            selector_surf.blit(label_surf, label_rect)
        selector_surf = selector_surf.convert_alpha()
        return selector_surf

    def update_scroll(self) -> None:
        max_visible: int = max(1, self.rect.height // self.line_spacing)
        if self.index < self.scroll_offset:
            self.scroll_offset = self.index
        elif self.index >= self.scroll_offset + max_visible:
            self.scroll_offset = self.index - max_visible + 1

        max_offset = max(0, len(self.labels) - max_visible)
        self.scroll_offset = min(self.scroll_offset, max_offset)

    def scroll_down(self) -> None:
        """Method used to scroll down through the different items"""

        if not self.labels:
            return
        self.index = (self.index + 1) % len(self.labels)
        self.mark_changed()

    def scroll_up(self) -> None:
        """Method used to scroll up through the different items"""
        if not self.labels:
            return
        self.index = (self.index - 1) % len(self.labels)
        self.mark_changed()

    def get_selected_item(self) -> str | None:
        if not self.labels:
            return None
        return self.labels[self.index]

    def get_selected_index(self) -> int:
        return self.index
