import pygame
from resources.assets import Assets
from widgets.widget import Widget


class ImagePanel(Widget):
    def __init__(
        self,
        rect: pygame.Rect,
        assets: Assets,
        image_key: str,
        color: tuple[int, int, int],
    ) -> None:
        super().__init__(rect, assets)
        self.image_key: str = image_key
        self.color = color
        self.surf = self.generate_surf()
        
    def update(self, dt: float) -> None:
        return super().update(dt)
    
    def generate_surf(self) -> pygame.Surface:
        image_surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        image = self.assets.images.get(self.image_key)
        if image:
            shifted_image = self.tint_image(image)
            shifted_image_rect = shifted_image.get_rect(center=image_surf.get_rect().center)
            image_surf.blit(shifted_image, shifted_image_rect)
        return image_surf.convert_alpha()

    def tint_image(self, image: pygame.Surface) -> pygame.Surface:
        shifted = image.copy()
        tint = pygame.Surface(image.get_size()).convert_alpha()
        tint.fill(self.color)
        shifted.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return shifted

    def set_image_key(self, key: str) -> None:
        if key != self.image_key:
            self.image_key = key
            self.mark_changed()
