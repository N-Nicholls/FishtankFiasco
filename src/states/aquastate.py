from states.gamestate import GameState
import pygame
import random

from objects.fish import Fish

class AquaState(GameState):

    def __init__(self, game, controls):
        super().__init__(game)
        
        self.game = game
        self.controls = controls

        self.ADDFISH = pygame.USEREVENT + 1
        self.COOLDOWN = 0
        

        self.all_sprites = pygame.sprite.Group()
        self.sound = pygame.mixer.Sound("./sprites/bubble-in-water-422579.mp3")

    def spawnFish(self):
        pos = (random.randrange(800), random.randrange(600))
        temp = Fish(self.game, pos)
        self.all_sprites.add(temp)
        self.sound.play()

    def handleEvents(self, events):
        pressed_keys = pygame.key.get_pressed()
        for event in events:
            if pressed_keys[pygame.K_1] and self.COOLDOWN == 0:
                self.spawnFish()
                self.COOLDOWN = 3
            if pressed_keys[pygame.K_2] and self.COOLDOWN == 0 and self.all_sprites is not None:
                for entity in self.all_sprites:
                    entity.moveDir = random.choice([-1, 1])
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.COOLDOWN > 0:
            self.COOLDOWN -= 1
        
        self.all_sprites.update()
    
    def draw(self, screen):
        screen.fill((180, 89, 30))

        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        pygame.display.update()