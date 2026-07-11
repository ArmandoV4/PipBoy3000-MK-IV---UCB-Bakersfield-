import pygame
from pygame import Surface
from resources.assets import Assets
from managers.gps_manager import GPSManager
from tabs.submenu import Submenu
from utils.constants import LEFT_EDGE, RIGHT_EDGE, BOTTOM_EDGE, PIPBOY_GREEN

class WorldMap(Submenu):
    def __init__(self, assets: Assets, gps_manager: GPSManager) -> None:
        super().__init__(assets)
        self.gps_manager = gps_manager
        self.name: str = 'WORLD MAP'
        self.current_position_surface: pygame.Surface = self.generate_position_surface()
        self.current_position_rect = self.current_position_surface.get_rect(midbottom = (LEFT_EDGE + (RIGHT_EDGE - LEFT_EDGE) // 2, BOTTOM_EDGE))

    def update(self, dt: float) -> None:
        if self.gps_manager.new_coordinates:
            self.current_position_surface = self.generate_position_surface()

    def draw(self, screen: Surface) -> None:
        screen.blit(self.current_position_surface, self.current_position_rect)
        pass
    
    def generate_position_surface(self) -> pygame.Surface:
        lat = self.gps_manager.current_lat
        long = self.gps_manager.current_long
        coords: str = f'Current Position | Lat: {lat:.4f}, Long: {long:.4f}'
        coords_surface = self.assets.fonts['small'].render(coords, True, PIPBOY_GREEN)
        return coords_surface
