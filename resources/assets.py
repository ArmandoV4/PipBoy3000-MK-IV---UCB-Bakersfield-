import pygame

class Assets:
    def __init__(self) -> None:
        
        pygame.font.init()
        pygame.mixer.init()
        
        self.fonts: dict[str, pygame.font.Font] = {
            "small"     : pygame.font.Font("resources/fonts/monofonto.ttf", 18),
            "medium"    : pygame.font.Font("resources/fonts/monofonto.ttf", 24),
            "large"     : pygame.font.Font("resources/fonts/monofonto.ttf", 36),   
            "clock"     : pygame.font.Font("resources/fonts/monofonto.ttf", 90),
        }

        self.images: dict[str, pygame.Surface] =  {
            "start"         : pygame.image.load("resources/images/pipboystart.png"),
            "Strength"      : pygame.image.load("resources/images/strength.png").convert_alpha(),
            "Perception"    : pygame.image.load("resources/images/perception.png").convert_alpha(),
            "Endurance"     : pygame.image.load("resources/images/endurance.png").convert_alpha(),
            "Charisma"      : pygame.image.load("resources/images/charisma.png").convert_alpha(),
            "Intelligence"  : pygame.image.load("resources/images/intelligence.png").convert_alpha(),
            "Agility"       : pygame.image.load("resources/images/agility.png").convert_alpha(),
            "Luck"          : pygame.image.load("resources/images/luck.png").convert_alpha()
        }
