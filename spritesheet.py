import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height))
        image.set_colorkey(color) 
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        #image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def get_sheet(self, frameX, frameY , width, height, scale, color):
        image = pygame.Surface((width, height))
        image.set_colorkey(color) 
        image.blit(self.sheet, (0, 0), ((frameX * width), (frameY * height), width, height))
        #image = pygame.transform.scale(image, (width * scale, height * scale))
        return image