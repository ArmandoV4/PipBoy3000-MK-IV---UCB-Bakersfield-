import pygame
import submenus


class MenuTab:
    def __init__(self, name, assets):
        self.name = name
        self.assets = assets
        self.tabs_list = None

    def display_tab(self):
        return self.name

    def subtabs(self):
        return self.tabs_list

    def subtab_names(self):
        return [name.display_name() for name in self.subtabs()]

    def display_subtabs(self, index):
        return self.subtabs()[index]

    def update_selected_submenu(self, submenu_index, key_pressed):
        self.tabs_list[submenu_index].input_handler(key_pressed)

    def draw_menu(
        self, screen, tabs, menu_index, submenu_index, color, menu_font, submenu_font
    ):
        screen.fill((0, 6, 0))
        menu_tab_x_pos = 20
        submenu_tab_x_pos = 20
        y_pos = 10
        menu_tab_names = [i.display_tab() for i in tabs]
        submenu_tab_names = self.subtab_names()
        amount_of_tabs = len(menu_tab_names)
        amount_of_subtabs = len(submenu_tab_names)
        menu_tab_length = 760 // amount_of_tabs
        submenu_tab_length = 760 // amount_of_subtabs

        # Draws the menu tabs at the top of the screen
        for i, name in enumerate(menu_tab_names):
            size = self.assets.fonts["large"].size(name)[0]
            center = menu_tab_x_pos + ((menu_tab_length - size) / 2)
            if i == menu_index:
                # Underlines the name of the tab if the tab is selected
                self.assets.fonts["large"].set_underline(True)
                text = self.assets.fonts["large"].render(name, True, color)
                screen.blit(text, (center, y_pos))
                self.assets.fonts["large"].set_underline(False)
            else:
                # Draws the tab normally
                text = self.assets.fonts["large"].render(name, True, color)
                screen.blit(text, (center, y_pos))
            menu_tab_x_pos += menu_tab_length
        y_pos += self.assets.fonts["large"].get_linesize()

        for i, name in enumerate(submenu_tab_names):
            size = self.assets.fonts["medium"].size(name)[0]
            center = submenu_tab_x_pos + ((submenu_tab_length - size) / 2)
            if i == submenu_index:
                # Underlines the name of the subtab if the tab is selected
                self.assets.fonts["medium"].set_underline(True)
                text = self.assets.fonts["medium"].render(name, True, color)
                screen.blit(text, (center, y_pos))
                self.assets.fonts["medium"].set_underline(False)
            else:
                # Draws the subtab normally
                text = self.assets.fonts["medium"].render(name, True, color)
                screen.blit(text, (center, y_pos))
            submenu_tab_x_pos += submenu_tab_length
        y_pos += submenu_font.get_linesize()
        self.subtabs()[submenu_index].draw_submenu(screen, y_pos, color)


class StatusTab(MenuTab):
    def __init__(self, name, assets):
        super().__init__(name, assets)
        self.tabs_list = [
            submenus.StatusMenu(assets = self.assets),
            submenus.SpecialMenu(assets = self.assets),
            submenus.PerksMenu(assets = self.assets),
        ]


class InventoryTab(MenuTab):
    def __init__(self, name, assets):
        super().__init__(name, assets)
        self.tabs_list = [
            submenus.ItemsMenu(assets = self.assets),
            submenus.WeaponsMenu(assets = self.assets),
            submenus.ApparelMenu(assets = self.assets),
            submenus.AidMenu(assets = self.assets),
            submenus.MiscMenu(assets = self.assets),
        ]


class DataTab(MenuTab):
    def __init__(self, name, assets):
        super().__init__(name, assets)
        self.tabs_list = [
            submenus.QuestsMenu(assets = self.assets), 
            submenus.NotesMenu(assets = self.assets)
            ]


class MapTab(MenuTab):
    def __init__(self, name, assets):
        super().__init__(name, assets)
        self.tabs_list = [
            submenus.WorldMapMenu(assets = self.assets), 
            submenus.LocalMapMenu(assets = self.assets)]


class RadioTab(MenuTab):
    def __init__(self, name, assets):
        super().__init__(name, assets)
        self.tabs_list = [
            submenus.StationsMenu(assets = self.assets), 
            submenus.TuningMenu(assets = self.assets)
            ]
