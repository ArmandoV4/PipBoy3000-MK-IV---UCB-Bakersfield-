import pygame

class Assets:
    def __init__(self):
        self.fonts = {
            "small" : pygame.font.Font("monofonto.ttf", 18),
            "medium": pygame.font.Font("monofonto.ttf", 24),
            "large" : pygame.font.Font("monofonto.ttf", 36),   
            "clock" : pygame.font.Font("monofonto.ttf", 90),
        }

        self.sounds = {
            "menu"      : pygame.mixer.Sound("resources/sounds/ui_pipboy_tab.wav"),
            "cursor"    : pygame.mixer.Sound("resources/sounds/ui_menu_focus.wav"),
            "select"    : pygame.mixer.Sound("resources/sounds/ui_pipboy_select.wav"),
            "typing1"   : pygame.mixer.Sound("resources/sounds/ui_hacking_charsingle_01.wav"),
            "typing2"   : pygame.mixer.Sound("resources/sounds/ui_hacking_charsingle_02.wav"),
            "typing3"   : pygame.mixer.Sound("resources/sounds/ui_hacking_charsingle_03.wav"),
            "typing4"   : pygame.mixer.Sound("resources/sounds/ui_hacking_charsingle_04.wav"),
            "typing5"   : pygame.mixer.Sound("resources/sounds/ui_hacking_charsingle_05.wav"),
            "typing6"   : pygame.mixer.Sound("resources/sounds/ui_hacking_charsingle_06.wav")
        }