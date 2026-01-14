import pygame
import sys

from states.aquastate import AquaState

class Game():

    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()
        

        # Set up the window
        self.screen_width, self.screen_height = 800, 600

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.SCALED | pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.display.set_caption("Basic Pygame Window")
        self.clock = pygame.time.Clock()
        self.controls = None
        self.running = True

        self.state = AquaState(self, self.controls)

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False   
            self.clock.tick(60)
            self.state.draw(self.screen)
            self.state.handleEvents(events)
            self.state.update()

    def changeState(self, state):
        self.state = state

    def quit():
        # Clean up
        pygame.quit()
        sys.exit()





