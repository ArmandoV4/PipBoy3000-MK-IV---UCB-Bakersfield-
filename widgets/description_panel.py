import pygame
from pygame import Rect
from resources.assets import Assets
from widgets.widget import Widget
from utils.constants import TAB

class DescriptionPanel(Widget):
    def __init__(self, rect: Rect, assets: Assets, desc: str, font_key: str, text_color: tuple[int, int, int]) -> None:
        super().__init__(rect, assets)
        self.desc: str = desc
        self.font_key: str = font_key
        self.text_color: tuple[int, int, int] = text_color
        self.indent_size = self.assets.fonts[font_key].size(TAB)[0]
        self.desc_line_height: int = self.assets.fonts[font_key].get_linesize()
        self.max_desc_width = self.rect.width - (2 * self.indent_size)
        self.surf = self.generate_surf()
    
    def update(self, dt: float) -> None:
        return super().update(dt)
    
    def generate_surf(self) -> pygame.Surface:
        desc_surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        desc_lines = self.wrap_text(self.assets.fonts[self.font_key], self.desc, self.max_desc_width)
        max_lines = self.rect.height // self.desc_line_height
        visible_lines = desc_lines[:max_lines]
        for line_index, line in enumerate(visible_lines):
            line_surf = self.assets.fonts[self.font_key].render(line, True, self.text_color)
            line_rect = line_surf.get_rect(topleft = ( self.indent_size, self.desc_line_height * line_index ))
            desc_surf.blit(line_surf, line_rect)

        return desc_surf.convert_alpha()    
    
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
    
    def set_desc(self, desc: str) -> None:
        if desc != self.desc:
            self.desc = desc
            self.mark_changed()