import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.constants import LEFT_EDGE, PIPBOY_GREEN
from utils.events import SCROLL_UP, SCROLL_DOWN


class Special(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name: str = "Special"
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
        screen.blit(self.special_surface, (LEFT_EDGE, self.working_area_edge))

    def update(self, dt: float) -> None:
        if self.menu_index_changed:
            self.special_surface = self.generate_special_surface()
            self.menu_index_changed = False

    def generate_special_surface(self) -> pygame.Surface:
        self.special_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        line_spacing: int = self.assets.fonts["medium"].get_linesize()
        desc_line_height = self.assets.fonts['small'].get_linesize()
        max_width_size: int = max(
            self.assets.fonts["medium"].size(stat["name"])[0] for stat in self.stats
        )
        tab_size: int = self.assets.fonts['medium'].size("   ")[0]
        special_edge = max_width_size + 2 * tab_size
        desc_left = special_edge + tab_size
        right_panel_center_x = special_edge + (self.width - special_edge) // 2
        max_desc_width = self.width - desc_left - tab_size
        bottom_padding = line_spacing // 2

        for index, stat in enumerate(self.stats):
            if index == self.menu_index:
                stat_text = self.assets.fonts['medium'].render(
                    ">" + stat["name"], True, PIPBOY_GREEN
                )
                stat_image = self.assets.images[stat['name']]
                stat_image = self.shift_image_hue(stat_image, PIPBOY_GREEN)

                desc_lines = self.wrap_text(self.assets.fonts['small'], stat['desc'], max_desc_width)
                desc_height = len(desc_lines) * desc_line_height
                desc_top = (self.height - desc_height - bottom_padding)
                stat_image_rect = stat_image.get_rect(center = (right_panel_center_x, desc_top // 2 ))

                for line_index, line in enumerate(desc_lines):
                    desc_surface = self.assets.fonts['small'].render(line, True, PIPBOY_GREEN)
                    desc_rect = desc_surface.get_rect(topleft = (desc_left, desc_top + (line_index * desc_line_height)))
                    self.special_surface.blit(desc_surface, desc_rect)
                
                
                self.special_surface.blit(stat_text, (tab_size, line_spacing * index))
                self.special_surface.blit(stat_image, stat_image_rect)
                pygame.draw.line(
                    self.special_surface,
                    PIPBOY_GREEN,
                    (special_edge, 0),
                    (special_edge, self.height),
                )
                
            else:
                stat_text = self.assets.fonts['medium'].render(
                    stat["name"], True, PIPBOY_GREEN
                )
                self.special_surface.blit(stat_text, (tab_size, line_spacing * index))
        self.special_surface = self.special_surface.convert_alpha()

        return self.special_surface

    def shift_image_hue(
        self, image: pygame.Surface, color: tuple[int, int, int]
    ) -> pygame.Surface:
        shifted = image.copy()
        tint = pygame.Surface(image.get_size()).convert_alpha()
        tint.fill(color)
        shifted.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return shifted
    
    def wrap_text(self, font: pygame.font.Font, text: str, max_width: int) -> list[str]:
        words: list[str] = text.split(' ')
        lines: list[str] = []
        current_line: str = ''

        for word in words:
            test_line: str = (current_line + ' ' + word).strip()
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines