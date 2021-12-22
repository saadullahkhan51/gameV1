import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height))
        image.set_colorkey(color) 
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        return image