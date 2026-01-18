import pygame
import sys
import json
import shutil
from pathlib import Path

from src.states.aqua_state import AquaState
from src.core.asset_manager import AssetManager

class Game():

    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()
        
        # Load Path and Config Data
        file_path = Path(AssetManager.get_path("config.json"))
        file_path_default = Path(AssetManager.get_path("config_default.json"))

        
        # If config doesn't exist, copy default
        if not file_path.is_file():
            shutil.copy(file_path_default, file_path)


        with open(file_path, 'r') as json_file:
            config_data_loaded = json.load(json_file)
        self.screen_width = config_data_loaded["screen"]["width"] 
        self.screen_height = config_data_loaded["screen"]["height"]
        self.frame_rate = config_data_loaded["frameRate"]
        self.controls = self.load_controls(config_data_loaded["controls"]) # needs to convert json strings to PYGAME consts
        print(f'Screen Width: {self.screen_width}, Screen Height: {self.screen_height}, Frame Rate: {self.frame_rate}')


        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.SCALED | pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.display.set_caption("Basic Pygame Window")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = AquaState(self, self.controls)

    def load_controls(self, controls_config):
        controls = {'right': pygame.K_d, 'left': pygame.K_a, 'up': pygame.K_w, 'down': pygame.K_s, 'escape': pygame.K_ESCAPE, 'k1': pygame.K_1, 'k2': pygame.K_2, 'k3': pygame.K_3, 'k4': pygame.K_4}
        for action, key_name in controls_config.items():
            if isinstance(key_name, str):
                if hasattr(pygame, key_name):
                    controls[action] = getattr(pygame, key_name)
                else:
                    if action in self.controls:
                        # controls[action] = self.default[action]
                        print(f"Key specification for '{action}' not found, replacing with default '{self.controls[action]}'")
                    else:
                        print(f"Warning: Key specification for '{action}' is invalid and no default is provided")
            else:
                if action in self.controls:
                    # controls[action] = self.default[action]
                    print(f"Key specification for '{action}' was not a string or not found, replacing with default '{self.controls[action]}'")
                else:
                    print(f"Warning: Key specification for '{action}' is not a string and no default is provided. Found {type(key_name).__name__} instead.")
        return controls


    def run(self):
        while self.running:
            self.time_delta = self.clock.tick(self.frame_rate)/1000.0
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False   
            
            self.state.draw(self.screen)
            self.state.handleEvents(events)
            self.state.update()

    def changeState(self, state):
        self.state = state

    def quit():
        pygame.quit()
        sys.exit()





