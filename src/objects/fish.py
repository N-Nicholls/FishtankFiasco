from src.core.sprite_sheet import SpriteSheet
from src.core.asset_manager import AssetManager
from src.core.vector import Vector
import pygame
import random
import math

class Fish(pygame.sprite.Sprite):
    fish_one = AssetManager.get_path("fishy1.png", "sprites")
    fish_two = AssetManager.get_path("fishy2.png", "sprites")
    fish_three = AssetManager.get_path("fishy3.png", "sprites")

    def __init__(self, game, pos = (0,0), type = None):
        super(Fish, self).__init__()
        self.game = game

        # boid stuff
        self.speedLimit = 3
        self.minDistance = 20
        self.avoidFactor = 0.05 # adjust velocity by this %
        self.matchingFactor = 0.05 # Adjust by this % of avg velocity
        self.centeringFactor = 0.005 # by %
        self.margin = 20
        self.turnFactor = .1
        self.visualRange = 60

        self.velocity = Vector(4, 0)#Vector(random.choice([-1, 1, 3, -3, 2, -2]), random.choice([-1, 1, 3, -3, 2, -2]))

        # rendering
        if type is None:
            self.type = random.choice([0, 1])
        else:
            self.type = type

        if self.type == 1:
            sheetPath = self.fish_one
            self.width = 540
            self.height = 360
            self.scale = .1
        if self.type == 3:
            sheetPath = self.fish_three
            self.width = 612
            self.height = 306
            self.scale = .4
        else:
            sheetPath = self.fish_two
            self.width = 2000
            self.height = 817
            self.scale = 0.02

        self.scale *= random.gauss(1.0, 0.2)

        self.flipped = False

        self.sheet = SpriteSheet(sheetPath)
        self.surf = self.sheet.image_at(0, self.width, self.height, self.scale)
        self.rect = self.surf.get_rect(center=pos)

        self.moveDir = 1 * random.choice([-1, 1])


    def update(self, value = None, static = 0):

        if value:
            self.speedLimit = value

        self.flyTowardsCenter()
        self.avoidOthers()
        self.matchVelocity()
        self.keepWithinBounds()
        self.limitSpeed()



        # maintains movement
        self.move(self.velocity.x, self.velocity.y)

    # Simply limit speed
    def limitSpeed(self):
        if(abs(self.velocity) > self.speedLimit):
            self.velocity = self.velocity.normalize() * self.speedLimit
    
    # move away from others 
    def avoidOthers(self):
        move = Vector(0, 0)
        for boid in self.game.state.prey:
            if boid != self and self.rect_distance_center(boid.rect) < self.minDistance:
                move.x += (self.rect.centerx - boid.rect.centerx)
                move.y += (self.rect.centery - boid.rect.centery)
            
        self.velocity += move * self.avoidFactor

    
    # constrain within a window, move if you want to, I don't care.
    def keepWithinBounds(self):
        if self.rect.x < self.margin:
            self.velocity.x += self.turnFactor
        if self.rect.x > self.game.screen_width - self.margin:
            self.velocity.x -= self.turnFactor
        if self.rect.y < self.margin:
            self.velocity.y += self.turnFactor
        if self.rect.y > self.game.screen_height - self.margin:
            self.velocity.y -= self.turnFactor

    # Find center of mass of other boids and adjust velocity towards that
    def flyTowardsCenter(self):
        center = [0, 0]
        numNeighbors = 0

        for boid in self.game.state.prey:
            if boid != self and self.rect_distance_center(boid.rect) < self.visualRange:
                center[0] += boid.rect.centerx
                center[1] += boid.rect.centery
                numNeighbors += 1
            
        if(numNeighbors != 0):
            center[0] /= numNeighbors
            center[1] /= numNeighbors
            
            center[0] -= self.rect.centerx
            center[1] -= self.rect.centery
            self.velocity += Vector(center[0] * self.centeringFactor, center[1] * self.centeringFactor)

    # Find center of mass of other boids and adjust velocity towards that
    def matchVelocity(self):
        avgDx = Vector(0, 0)
        numNeighbors = 0

        for boid in self.game.state.prey:
            if self.rect_distance_center(boid.rect) < self.visualRange and boid != self: # maybe move
                avgDx += boid.velocity
                numNeighbors += 1
            
        if(numNeighbors != 0):
            avgDx.x = avgDx.x / numNeighbors
            avgDx.y = avgDx.y / numNeighbors
            
            self.velocity += (avgDx - self.velocity) * self.matchingFactor



    def rect_distance_center(self, rect2):
        dx = self.rect.centerx - rect2.centerx
        dy = self.rect.centery - rect2.centery
        return math.hypot(dx, dy)





    def setSheet(self, path, frame = 0, scale = None):
        if scale is not None:
            self.scale = scale
        self.scale *= random.gauss(1.0, 0.2)
        self.sheet = SpriteSheet(path)
        self.surf = self.sheet.image_at(frame, self.width, self.height, self.scale)
        old_center = self.rect.center
        self.rect = self.surf.get_rect(center=old_center)

    # collision stuff per direction individually
    def move(self, dx, dy):
        self.moveSingleAxis(dx, 0)
        self.moveSingleAxis(0, dy)

    def moveSingleAxis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        