import datetime
import pygame
import random


class SubMenu:
    def __init__(self, name=None, submenu_index=0, assets=None):
        self.name = name
        self.submenu_index = submenu_index
        self.assets = assets
        self.submenu_list = []

    def display_name(self):
        return self.name

    def draw_submenu(self, screen, y_pos, color):
        text = self.assets.fonts["large"].render(
            f"{self.name} NOT IMPLEMENDED, COMING SOON!", True, color
        )
        rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, rect)
    
    def image_hue_shift(self, image, color):
        shifted = image.copy()
        tint = pygame.Surface(image.get_size()).convert_alpha()
        tint.fill(color)
        shifted.blit(tint, (0, 0), special_flags = pygame.BLEND_RGBA_MULT)
        return shifted

    def input_handler(self, key_pressed):
        pass


class StatusMenu(SubMenu):
    def __init__(self, name="STATUS", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)
        self.current_time = datetime.datetime.now()
        self.military_time = False

    def update_time_format(self):
        self.military_time = not self.military_time

    def update_time(self):
        self.current_time = datetime.datetime.now()

    def formatted_time(self):
        if self.military_time:
            formatted_time = self.current_time.strftime("%H:%M:%S")
        else:
            formatted_time = self.current_time.strftime("%I:%M:%S%p")
        return formatted_time

    def formatted_date(self):
        return self.current_time.strftime("%m/%d/%Y")

    def draw_submenu(
        self,
        screen,
        y_pos,
        color,
    ):
        x_pos = 20
        remaining_space = 460 - y_pos
        self.update_time()

        time_text = self.formatted_time()
        rendered_time_text = self.assets.fonts["clock"].render(time_text, True, color)
        time_text_size = self.assets.fonts["clock"].size(time_text)

        date_text = self.formatted_date()
        rendered_date_text = self.assets.fonts["medium"].render(date_text, True, color)
        date_text_size = self.assets.fonts["medium"].size(date_text)

        centered_time_text_x = x_pos + ((760 - time_text_size[0]) // 2)
        centered_time_text_y = y_pos + (
            (remaining_space - time_text_size[1] - date_text_size[1]) // 2
        )
        screen.blit(rendered_time_text, (centered_time_text_x, centered_time_text_y))
        y_pos = centered_time_text_y + self.assets.fonts["clock"].get_linesize()
        centered_date_text_x = x_pos + ((760 - date_text_size[0]) // 2)
        screen.blit(rendered_date_text, (centered_date_text_x, y_pos))

    def input_handler(self, key_pressed):
        if self.submenu_index == 0 and key_pressed == pygame.K_RETURN:
            self.update_time_format()


class SpecialMenu(SubMenu):
    def __init__(self, name="SPECIAL", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)

        # (name, value, description)
        self.stats = [
            (
                "STRENGTH",
                5,
                "Strength is a measure of your raw physical power. It affects how much you can carry and the damage of all melee attacks.",
            ),
            (
                "PERCEPTION",
                5,
                "Perception is your environmental awareness and 'sixth sense,' and affects weapon accuracy in V.A.T.S.",
            ),
            (
                "ENDURANCE",
                5,
                "Endurance is the measure of your physical fitness. It affects your total Health and the action point drain from sprinting.",
            ),
            (
                "CHARISMA",
                5,
                "Charisma is the ability to charm and convice others. It affects your chance to persuade in dialogue and prices when you barter.",
            ),
            (
                "INTELLIGENCE",
                5,
                "Intelligence is a measure of your overall mental acuity, and affects the number of Experience Points earned.",
            ),
            (
                "AGILITY",
                5,
                "Agility is the measurement of your overall fitness and reflexes. It affects the number of Action Points in V.A.T.S. and your ability to sneak.",
            ),
            (
                "LUCK",
                5,
                "Luck is a measurement of your general good fortune, and affects the recharge rate of Critical Hits.",
            ),
        ]
        self.special_images = [
            self.assets.images["strength"],
            self.assets.images["perception"],
            self.assets.images["endurance"],
            self.assets.images["charisma"],
            self.assets.images["intelligence"],
            self.assets.images["agility"],
            self.assets.images["luck"]
        ]
        self.submenu_index = 0

        
    def wrap_text(self, font, text, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = (current_line + " " + word).strip()
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    def draw_submenu(self, screen, y_pos, color):
        left_margin = 60
        top = y_pos + 20
        line_spacing = self.assets.fonts["small"].get_height() + 8

        # fixed value column (aligned by longest name + 3 "tabs")
        tab_width = self.assets.fonts["small"].size("    ")[0]
        max_name_width = max(
            self.assets.fonts["small"].size(name)[0] for name, _, _ in self.stats
        )
        value_column_x = left_margin + max_name_width + 3 * tab_width

        # left list: name + aligned value
        for i, (name, value, desc) in enumerate(self.stats):
            y = top + i * line_spacing

            if i == self.submenu_index:
                pointer_surface = self.assets.fonts["small"].render(">", True, color)
                pointer_rect = pointer_surface.get_rect()
                pointer_rect.midright = (
                    left_margin - 10,
                    y + self.assets.fonts["small"].get_height() // 2,
                )
                screen.blit(pointer_surface, pointer_rect.topleft)

            name_surface = self.assets.fonts["small"].render(name, True, color)
            screen.blit(name_surface, (left_margin, y))

            value_surface = self.assets.fonts["small"].render(str(value), True, color)
            screen.blit(value_surface, (value_column_x, y))

        # description for selected stat, bottom-right
        _, value, desc = self.stats[self.submenu_index]

        desc_x = left_margin + 260
        bottom_start_y = top + line_spacing * len(self.stats) + 20

        screen_width = screen.get_width()
        max_width = screen_width - desc_x - 20

        image = self.special_images[self.submenu_index].copy()
        image = self.image_hue_shift(image, color)
        image_rect = image.get_rect()
        right_panel_left = desc_x
        right_panel_width = 800 - right_panel_left

        image_rect.midtop = (right_panel_left + right_panel_width // 2, top + 20)
        screen.blit(image, image_rect)

        lines = self.wrap_text(self.assets.fonts["small"], desc, max_width)

        for i, line in enumerate(lines):
            text_surface = self.assets.fonts["small"].render(line, True, color)
            line_y = bottom_start_y + i * line_spacing
            screen.blit(text_surface, (desc_x, line_y))

    def input_handler(self, key_pressed):
        """
        Called when the user presses ENTER on the SPECIAL submenu.

        For now, we'll simply cycle through S -> P -> E -> C -> I -> A -> L.
        """
        if key_pressed == pygame.K_q:
            self.submenu_index = (self.submenu_index - 1) % len(self.stats)

        if key_pressed == pygame.K_e:
            self.submenu_index = (self.submenu_index + 1) % len(self.stats)


class PerksMenu(SubMenu):
    def __init__(self, name="PERKS", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class ItemsMenu(SubMenu):
    def __init__(self, name="ITEMS", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class WeaponsMenu(SubMenu):
    def __init__(self, name="WEAPONS", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class ApparelMenu(SubMenu):
    def __init__(self, name="APPAREL", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class AidMenu(SubMenu):
    def __init__(self, name="AID", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class MiscMenu(SubMenu):
    def __init__(self, name="MISC", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class QuestsMenu(SubMenu):
    def __init__(self, name="QUESTS", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class NotesMenu(SubMenu):
    def __init__(self, name="NOTES", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class WorldMapMenu(SubMenu):
    def __init__(self, name="WORLD MAP", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class LocalMapMenu(SubMenu):
    def __init__(self, name="LOCAL MAP", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)


class StationsMenu(SubMenu):
    def __init__(self, name="STATIONS", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)
        self.MUSIC_END = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.MUSIC_END)
        self.radio_stations = [
            "Diamond City Radio",
            "Radio New Vegas",
            "Galaxy News Radio",
            "Appalachia Radio",
        ]
        self.radio_paused = False
        self.current_song = None
        self.playlist_index = 0
        self.playlist = [
            self.playlist_creator(self.assets.diamond_city_radio),
            self.playlist_creator(self.assets.radio_new_vegas),
            self.playlist_creator(self.assets.galaxy_news_radio),
            self.playlist_creator(self.assets.appalachia_radio),
        ]
        self.bars = [0] * 64
        self.song_loader()

    def input_handler(self, key_pressed):
        match key_pressed:
            case pygame.K_RETURN:
                self.toggle_radio()

            case pygame.K_a:
                self.previous_song()

            case pygame.K_d:
                self.next_song()

            case pygame.K_q:
                self.submenu_index = (self.submenu_index - 1) % len(self.radio_stations)
                self.playlist_index = 0
                self.song_loader()

            case pygame.K_e:
                self.submenu_index = (self.submenu_index + 1) % len(self.radio_stations)
                self.playlist_index = 0
                self.song_loader()

    def draw_submenu(self, screen, y_pos, color):

        LEFT_MARGIN = 60
        TOP_MARGIN = y_pos + 20
        LINE_SPACING = self.assets.fonts["small"].get_height() + 8
        TAB_WIDTH = self.assets.fonts["small"].size("    ")[0]
        MAX_NAME_WIDTH = max(
            self.assets.fonts["small"].size(name)[0] for name in self.radio_stations
        )
        BORDER_X_POSITION = LEFT_MARGIN + MAX_NAME_WIDTH + TAB_WIDTH
        NOW_PLAYING_POSITION = BORDER_X_POSITION + TAB_WIDTH

        for i, name in enumerate(self.radio_stations):
            y = TOP_MARGIN + i * LINE_SPACING

            if i == self.submenu_index:
                pointer_surface = self.assets.fonts["small"].render(">", True, color)
                pointer_rect = pointer_surface.get_rect()
                pointer_rect.midright = (
                    LEFT_MARGIN - 10,
                    y + self.assets.fonts["small"].get_height() // 2,
                )
                screen.blit(pointer_surface, pointer_rect.topleft)

            name_surface = self.assets.fonts["small"].render(name, True, color)
            screen.blit(name_surface, (LEFT_MARGIN, y))
        
        border_surface = pygame.Surface((2, 480 - TOP_MARGIN - LINE_SPACING - 20))
        border_surface.fill(color)

        title, artist = self.current_song.split(" - ", 1)
        now_playing_surface = self.assets.fonts["small"].render(
            "Now Playing:", True, color
        )
        song_text_surface = self.assets.fonts["small"].render(
            title, True, color
        )
        song_artist_surface = self.assets.fonts["small"].render(
            artist, True, color
        )

        box_w = 800 - NOW_PLAYING_POSITION - LEFT_MARGIN
        box_h = 7*LINE_SPACING
        wave_rect = pygame.Rect(NOW_PLAYING_POSITION, TOP_MARGIN, box_w, box_h)
        
        pygame.draw.rect(screen, color, wave_rect, 2)
        self.update_wave_form(box_h)
        bar_width = wave_rect.width / len(self.bars)
        for i, h in enumerate(self.bars):
            x = wave_rect.left + int(i * bar_width)
            y_center = wave_rect.centery
            pygame.draw.line(screen,color,(x,y_center - h),(x, y_center + h), 2)
        
        text_x = wave_rect.bottomleft[0]
        text_y = wave_rect.bottom + 10
        
        screen.blits(
            [
                (border_surface, (BORDER_X_POSITION, TOP_MARGIN)),
                (now_playing_surface, (text_x, text_y)),
                (song_text_surface, (text_x, text_y + LINE_SPACING)),
                (song_artist_surface, (text_x, text_y + 2 * LINE_SPACING))
            ]
        )

    def playlist_creator(self, song_asset):
        songlist = list(song_asset.items())
        random.shuffle(songlist)
        return songlist

    def song_loader(self):
        self.current_song, song_path = self.playlist[self.submenu_index][
            self.playlist_index
        ]
        pygame.mixer.music.load(song_path)

    def next_song(self):
        current_station = self.playlist[self.submenu_index]
        self.playlist_index = (self.playlist_index + 1) % len(current_station)
        self.song_loader()
        pygame.mixer.music.play()

    def previous_song(self):
        current_station = self.playlist[self.submenu_index]
        self.playlist_index = (self.playlist_index - 1) % len(current_station)
        self.song_loader()
        pygame.mixer.music.play()

    def music_playing(self):
        return pygame.mixer.music.get_busy()

    def toggle_radio(self):
        if self.radio_paused:
            pygame.mixer.music.unpause()
            self.radio_paused = False

        elif not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            self.radio_paused = False

        else:
            pygame.mixer.music.pause()
            self.radio_paused = True


    def update_wave_form(self, box_h):
        if self.radio_paused or not pygame.mixer.music.get_busy():
            self.bars = [0] * len(self.bars)
        else:
            for i in range(len(self.bars)):
                self.bars[i] = random.randint(5, box_h // 2)

class TuningMenu(SubMenu):
    def __init__(self, name="TUNING", submenu_index=0, assets=None):
        super().__init__(name, submenu_index, assets)
