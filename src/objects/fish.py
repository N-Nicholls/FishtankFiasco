from core.sprite_sheet import SpriteSheet
import pygame
import random

class Fish(pygame.sprite.Sprite):
    def __init__(self, game, pos = (0,0), sheetPath = "./sprites/fishy1.png"):
        super(Fish, self).__init__()
        self.game = game

        # rendering
        self.sheet = SpriteSheet(sheetPath)
        self.width = 540#game.block_size 
        self.height = 360#game.block_size
        self.surf = self.sheet.image_at(0, self.width, self.height)
        self.rect = self.surf.get_rect(center=pos)

        self.moveDir = 1 * random.choice([-1, 1])


    def update(self, static = 0):
        # maintains movement
        self.move(self.moveDir, 0)


    def setSheet(self, path, frame = 0):
        self.sheet = SpriteSheet(path)
        self.surf = self.sheet.image_at(frame, self.width, self.height)

    # collision stuff per direction individually
    def move(self, dx, dy):
        self.moveSingleAxis(dx, 0)
        self.moveSingleAxis(0, dy)

    def moveSingleAxis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        