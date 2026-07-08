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
            "Strength"              : pygame.image.load("resources/images/special/strength.png").convert_alpha(),
            "Perception"            : pygame.image.load("resources/images/special/perception.png").convert_alpha(),
            "Endurance"             : pygame.image.load("resources/images/special/endurance.png").convert_alpha(),
            "Charisma"              : pygame.image.load("resources/images/special/charisma.png").convert_alpha(),
            "Intelligence"          : pygame.image.load("resources/images/special/intelligence.png").convert_alpha(),
            "Agility"               : pygame.image.load("resources/images/special/agility.png").convert_alpha(),
            "Luck"                  : pygame.image.load("resources/images/special/luck.png").convert_alpha(),
            "Barter"                : pygame.image.load("resources/images/skills/Barter.png").convert_alpha(),
            "Energy Weapons"        : pygame.image.load("resources/images/skills/EnergyWeapons.png").convert_alpha(),
            "Explosives"            : pygame.image.load("resources/images/skills/Explosives.png").convert_alpha(),
            "Guns"                  : pygame.image.load("resources/images/skills/Guns.png").convert_alpha(),
            "Lockpick"              : pygame.image.load("resources/images/skills/Lockpick.png").convert_alpha(),
            "Medicine"              : pygame.image.load("resources/images/skills/Medicine.png").convert_alpha(),
            "Melee Weapons"         : pygame.image.load("resources/images/skills/MeleeWeapons.png").convert_alpha(),
            "Repair"                : pygame.image.load("resources/images/skills/Repair.png").convert_alpha(),
            "Science"               : pygame.image.load("resources/images/skills/Science.png").convert_alpha(),
            "Sneak"                 : pygame.image.load("resources/images/skills/Sneak.png").convert_alpha(),
            "Speech"                : pygame.image.load("resources/images/skills/Speech.png").convert_alpha(),
            "Survival"              : pygame.image.load("resources/images/skills/Survival.png").convert_alpha(),
            "Unarmed"               : pygame.image.load("resources/images/skills/Unarmed.png").convert_alpha(),
            "Confirmed Bachelor"    : pygame.image.load("resources/images/perks/ConfirmedBachelor.png").convert_alpha(),
            "Educated"              : pygame.image.load("resources/images/perks/Educated.png").convert_alpha(),
            "Bloody Mess"           : pygame.image.load("resources/images/perks/BloodyMess.png").convert_alpha(),
            "Good Natured"          : pygame.image.load("resources/images/perks/GoodNatured.png").convert_alpha(),
            "Wild Wasteland"        : pygame.image.load("resources/images/perks/WildWasteland.png").convert_alpha(),
        }