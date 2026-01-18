import pygame
import random
import math
from src.states.game_state import GameState
from src.objects.fish import Fish
from src.core.asset_manager import AssetManager
from src.gui.aqua_gui import AquaGUI

class AquaState(GameState):

    def __init__(self, game, controls):
        super().__init__(game)
        
        self.game = game
        self.controls = controls
        self.gui = AquaGUI(self)

        self.ADDFISH = pygame.USEREVENT + 1
        self.COOLDOWN = 0
        
        self.all_sprites = pygame.sprite.Group()
        self.boid_fish = pygame.sprite.Group()

        self.predator = pygame.sprite.Group()
        self.prey = pygame.sprite.Group()
        self.prey1 = pygame.sprite.Group()
        self.prey2 = pygame.sprite.Group()

        bubble_path = AssetManager.get_path("bubble-in-water-422579.mp3", "sounds")
        self.sound = pygame.mixer.Sound(bubble_path)

    def spawnFish(self, pos = None):
        fish_type = random.choice([1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3])
        if pos is None:
            pos = (random.randrange(self.game.screen_width), random.randrange(self.game.screen_height))
        temp = Fish(self.game, pos, fish_type)
        self.all_sprites.add(temp)
        self.boid_fish.add(temp)

        if fish_type == 1:
            self.prey.add(temp)
            self.prey1.add(temp)

        if fish_type == 2:
            self.prey.add(temp)
            self.prey2.add(temp)

        if fish_type == 3:
            self.predator.add(temp)
        #self.sound.play()

    def points_in_circle(self, center, radius, count, min_dist=0):
        """
        Generate `count` points inside a circle of given radius around `center`.
        Optionally enforce a minimum distance between points with `min_dist`.
        
        Args:
            center (tuple): (x, y) center of the circle
            radius (float): circle radius
            count (int): number of points to generate
            min_dist (float): minimum distance between points (approximate)
        
        Returns:
            List of (x, y) tuples
        """
        points = []
        attempts = 0
        max_attempts = count * 50  # to avoid infinite loops

        while len(points) < count and attempts < max_attempts:
            attempts += 1
            # random polar coordinates
            r = random.uniform(0, radius)
            theta = random.uniform(0, 2 * math.pi)
            x = center[0] + r * math.cos(theta)
            y = center[1] + r * math.sin(theta)

            # check distance to existing points
            if min_dist > 0:
                too_close = False
                for px, py in points:
                    if math.hypot(px - x, py - y) < min_dist:
                        too_close = True
                        break
                if too_close:
                    continue

            points.append((x, y))

        return points




    def handleEvents(self, events):
        pressed_keys = pygame.key.get_pressed()
        for event in events:
            if pressed_keys[self.game.controls['k1']] and self.COOLDOWN == 0:
                self.spawnFish()
                self.COOLDOWN = 3
            if pressed_keys[self.game.controls['k2']]:
                for fish in self.boid_fish:
                    fish.kill()
            if pressed_keys[self.game.controls['k3']] and self.COOLDOWN == 0:
                for fish in self.boid_fish:
                    fish.kill()
                for _ in range(90):
                    self.spawnFish()
                    self.COOLDOWN = 3


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = event.pos
                    if pos[0] >= 240 or pos[1] >= 400:

                        poss = self.points_in_circle(pos, 100, 10, 10)  
                        for i in poss:   
                            self.spawnFish(i)
            self.gui.handleEvents(event)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.COOLDOWN > 0:
            self.COOLDOWN -= 1
        self.gui.update()

        self.boid_fish.update()
        

        
    def draw(self, screen):
        screen.fill((180, 89, 30))

        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        self.gui.draw(screen)
        
        pygame.display.update()