import pygame

class Assets:
    def __init__(self):
        
        pygame.font.init()
        pygame.mixer.init()
        
        self.fonts = {
            "small"     : pygame.font.Font("monofonto.ttf", 18),
            "medium"    : pygame.font.Font("monofonto.ttf", 24),
            "large"     : pygame.font.Font("monofonto.ttf", 36),   
            "clock"     : pygame.font.Font("monofonto.ttf", 90),
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

        self.images = {
            "strength"      : pygame.image.load("resources/images/strength.png").convert_alpha(),
            "perception"    : pygame.image.load("resources/images/perception.png").convert_alpha(),
            "endurance"     : pygame.image.load("resources/images/endurance.png").convert_alpha(),
            "charisma"      : pygame.image.load("resources/images/charisma.png").convert_alpha(),
            "intelligence"  : pygame.image.load("resources/images/intelligence.png").convert_alpha(),
            "agility"       : pygame.image.load("resources/images/agility.png").convert_alpha(),
            "luck"          : pygame.image.load("resources/images/luck.png").convert_alpha()
        }

        self.diamond_city_radio = {
            "Atom Bomb Baby - The Five Stars"                       : "resources/music/diamondcityradio/Atom Bomb Baby.mp3",
            "I Don't Want To Set The World On Fire - The Ink Spots" : "resources/music/diamondcityradio/I Don't Want To Set The World On Fire.mp3",
            "Maybe - The Ink Spots"                                 : "resources/music/diamondcityradio/Maybe.mp3",
            "Orange Colored Sky - Nat King Cole"                    : "resources/music/diamondcityradio/Orange Colored Sky.mp3",
            "The Wanderer - Dion"                                   : "resources/music/diamondcityradio/The Wanderer.mp3"
        }

        self.radio_new_vegas = {
            "Big Iron - Marty Robbins"                                              : "resources/music/radionewvegas/Big Iron.mp3",
            "(I Got Spurs That) Jingle, Jangle, Jingle - Kay Kyser & His Orchestra" : "resources/music/radionewvegas/(I Got Spurs That) Jingle, Jangle, Jingle.mp3",
            "Blue Moon - Frank Sinatra"                                             : "resources/music/radionewvegas/Blue Moon.mp3",
            "Heartaches By The Number - Guy Mitchell"                               : "resources/music/radionewvegas/Heartaches By The Number.mp3",
            "Ain't That A Kick In The Head - Dean Martin"                           : "resources/music/radionewvegas/Ain't That A Kick In The Head.mp3"
        }

        self.galaxy_news_radio = {
            "I Don't Want To Set The World On Fire - The Ink Spots"                 : "resources/music/galaxynewsradio/I Don't Want To Set The World On Fire.mp3",
            "Anything Goes - Colle Porter"                                          : "resources/music/galaxynewsradio/Anything Goes.mp3",
            "Civilization (Bongo, Bongo, Bongo) - Danny Kaye & The Andrew Sisters"  : "resources/music/galaxynewsradio/Civilization (Bongo, Bongo, Bongo).mp3",
            "Butcher Pete (Part 1) - Roy Brown"                                     : "resources/music/galaxynewsradio/Butcher Pete (Part 1).mp3",
            "Into Each Life Some Rain Must Fall - The Ink Spots & Ella Fitzgerald"  : "resources/music/galaxynewsradio/Into Each Life Some Rain Must Fall.mp3"
        }

        self.appalachia_radio = {
            "Atom Bomb Baby - The Five Stars"               : "resources/music/appalachiaradio/Atom Bomb Baby.mp3",
            "Crazy He Calls Me - Billie Holiday"            : "resources/music/appalachiaradio/Crazy He Calls Me.mp3",
            "Dear Hearts And Gentle People - Bob Crosby"    : "resources/music/appalachiaradio/Dear Hearts And Gentle People.mp3",
            "Pistol Packin' Mama - Bing Crosby"             : "resources/music/appalachiaradio/Pistol Packin' Mama.mp3",
            "Sixteen Tons - Tennessee Ernie Ford"           : "resources/music/appalachiaradio/Sixteen Tons.mp3"
        }