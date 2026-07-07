import pygame
from pygame.event import Event
from resources.assets import Assets
from tabs.submenu import Submenu
from utils.events import SCROLL_UP, SCROLL_DOWN
from utils.constants import MEDIUM, PIPBOY_GREEN, LEFT_EDGE, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK, ORIGIN, DIVIDER_X, DESC_TOP

class Skills(Submenu):
    def __init__(self, assets: Assets) -> None:
        super().__init__(assets)
        self.name = 'Skills'
        self.skills: list[dict[str, str]] = [
            {
                "name": "Barter", 
                "desc": "Proficiency at trading and haggling. Also used to negotiate better quest rewards or occasionally as a bribe-like alternative to Speech.",
                "level": '50',
            },
            {
                "name": "Energy Weapons", 
                "desc": "Proficiency at using energy-based weapons. ",
                "level": '50',
            },
            {
                "name": "Explosives", 
                "desc": "Proficiency at using explosive weaponry, disarming mines, and crafting explosives.",
                "level": '50',
            },
             {
                "name": "Guns", 
                "desc": "Proficiency at using weapons that fire standard ammunition.",
                "level": '50',
            },
            {
                "name": "Lockpick", 
                "desc": "Proficiency at picking locks.",
                "level": '50',
            },                    
            {
                "name": "Medicine", 
                "desc": "Proficiency at using medical tools, drugs, and for crafting Doctor's Bags.",
                "level": '50',
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
                "desc": "Proficiency at persuading others. Also used to negotiate for better quest rewards and to talk your way out of combat, convincing people to give up vital information and succeeding in multiple Speech checks.",
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
        self.skill_surface: pygame.Surface = self.generate_skill_surface()

    def event_handler(self, event: Event) -> None:
        if event.type == SCROLL_DOWN:
            self.scroll_down(self.skills)

        elif event.type == SCROLL_UP:
            self.scroll_up(self.skills)
    
    def update(self, dt: float) -> None:
        if self.menu_index_changed:
            self.skill_surface = self.generate_skill_surface()
            self.menu_index_changed = False
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.skill_surface, ORIGIN)
        
     
    def generate_skill_surface(self) -> pygame.Surface:
        skill_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        line_spacing: int = self.assets.fonts[MEDIUM].get_linesize()
    
        self.update_scroll(len(self.skills), line_spacing)
        max_visible: int = max(1, self.height // line_spacing)
        visible_skills = self.skills[self.scroll_offset: self.scroll_offset + max_visible]

        for row, skill in enumerate(visible_skills):
            index = self.scroll_offset + row
            highlighted = index == self.menu_index
            name_surf = self.assets.fonts[MEDIUM].render(skill['name'], True, BLACK if highlighted else PIPBOY_GREEN)
            name_rect = name_surf.get_rect(topleft = (LEFT_EDGE, self.working_area_edge + (row * line_spacing)))
            level_surf = self.assets.fonts[MEDIUM].render(skill['level'], True, BLACK if highlighted else PIPBOY_GREEN)
            level_rect = level_surf.get_rect(topright = (DIVIDER_X, self.working_area_edge + (row * line_spacing)))
            highlight_rect = name_rect.union(level_rect)
            if highlighted:
                pygame.draw.rect(skill_surf, PIPBOY_GREEN, highlight_rect)
                pygame.draw.line(skill_surf, PIPBOY_GREEN, (DIVIDER_X, DESC_TOP), (SCREEN_WIDTH, DESC_TOP))
            skill_surf.blit(name_surf, name_rect)
            skill_surf.blit(level_surf, level_rect)
        
        self.draw_divider(skill_surf)
        skill_surf.convert_alpha()
        return skill_surf