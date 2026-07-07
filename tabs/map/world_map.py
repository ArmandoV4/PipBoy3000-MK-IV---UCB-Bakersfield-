import pygame
from pygame import Surface
from resources.assets import Assets
from application.gps_manager import GPSManager
from tabs.submenu import Submenu
from utils.constants import LEFT_EDGE, PIPBOY_GREEN

class WorldMap(Submenu):
    def __init__(self, assets: Assets, gps_manager: GPSManager) -> None:
        super().__init__(assets)
        self.gps_manager = gps_manager
        self.name: str = 'WORLD MAP'
        self.current_position_surface: pygame.Surface = self.generate_position_surface()

    def update(self, dt: float) -> None:
        if self.gps_manager.new_coordinates:
            self.current_position_surface = self.generate_position_surface()

    def draw(self, screen: Surface) -> None:
        screen.blit(self.current_position_surface, (LEFT_EDGE, self.working_area_edge))
        pass
    
    def generate_position_surface(self) -> pygame.Surface:
        temp_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        lat = self.gps_manager.current_lat
        long = self.gps_manager.current_long
        coords: str = f'Current Position | Lat: {lat:.4f}, Long: {long:.4f}'
        coords_surface = self.assets.fonts['small'].render(coords, True, PIPBOY_GREEN)
        coords_rect = coords_surface.get_rect(midbottom = (self.width//2, self.height))
        temp_surf.blit(coords_surface, coords_rect)
        return temp_surf
