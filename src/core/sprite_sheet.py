import pygame

class SpriteSheet:

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as error:
            print(f"Unable to load spritesheet: {filename}")
            raise SystemExit(error)
        
    def image_at(self, col, width, height, scale = 1, colorkey = None, row = 0):
        image = pygame.Surface((width, height), pygame.SRCALPHA)#.convert_alpha()
        image.blit(self.sheet, (0, 0), ((col * width), height*row, width, height))
        if colorkey is not None:
            image.set_colorkey(colorkey, pygame.RLEACCEL) # run length encoder, not sure the limitations on this.
        if scale != 1:
            image = pygame.transform.scale(image, (width*scale, height*scale))
        return image

    def images_at(self, rects, colorkey = None):
        return [self.image_at(rect, colorkey) for rect in rects]