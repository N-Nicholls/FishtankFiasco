import pygame
import pygame_gui

class AquaGUI:
    def __init__(self, state):
        
        self.state = state

        # pygui
        self.manager = pygame_gui.UIManager((self.state.game.screen_width, self.state.game.screen_height))

        # Define slider parameters: name, start, min, max
        self.slider_params = [
            ("speedLimit", 7, 0, 10),
            ("minDistance", 34, 0, 100),
            ("avoidFactor", 0.088, 0.0, 0.2),
            ("matchingFactor", 0.05, 0.0, 0.2),
            ("centeringFactor", 0.005, 0.0, 0.05),
            ("margin", 20, 0, 100),
            ("turnFactor", 0.250, 0.0, 1.0),
            ("visualRange", 66, 0, 200),
        ]

        self.sliders = []

        # Dynamically create sliders
        for i, (name, start, min_val, max_val) in enumerate(self.slider_params):
            slider = pygame_gui.elements.UIHorizontalSlider(
                relative_rect=pygame.Rect((50, 50 + i * 40), (150, 20)),  # smaller & spaced
                start_value=start,
                value_range=(min_val, max_val),
                manager=self.manager
            )
            self.sliders.append((name, slider))

        # font
        self.font = pygame.font.SysFont(None, 24)

    def handleEvents(self, event):
        self.manager.process_events(event)

    def update(self):
        self.manager.update(self.state.game.time_delta)

        # return a dictionary of current values
        values = {name: slider.get_current_value() for name, slider in self.sliders}

        for fish in self.state.boid_fish:
            fish.speedLimit = values["speedLimit"]
            fish.minDistance = values["minDistance"]
            fish.avoidFactor = values["avoidFactor"]
            fish.matchingFactor = values["matchingFactor"]
            fish.centeringFactor = values["centeringFactor"]
            fish.margin = values["margin"]
            fish.turnFactor = values["turnFactor"]
            fish.visualRange = values["visualRange"]
        

    def draw(self, screen):
        self.manager.draw_ui(screen)

        # Optional: draw text labels above sliders
        font = pygame.font.SysFont(None, 20)
        for name, slider in self.sliders:
            val = slider.get_current_value()
            text_surf = font.render(f"{name}: {val:.3f}", True, (255, 255, 255))
            x = slider.relative_rect.x
            y = slider.relative_rect.y - 18  # above the slider
            screen.blit(text_surf, (x, y))

        # fps
        fps_surf = self.font.render(f"FPS: {self.state.game.clock.get_fps():.2f}", True, (255,255,255))
        text_surf = self.font.render(f"Fish: {len(self.state.boid_fish)}", True, (255,255,255))
        screen.blit(fps_surf, (10, 10))
        screen.blit(text_surf, (10, 30))
