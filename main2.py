import pygame
import pygame_gui

pygame.init()
screen = pygame.display.set_mode((800, 600))
manager = pygame_gui.UIManager((800, 600))

slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((50, 50), (200, 30)),
    start_value=1.0,
    value_range=(0.0, 5.0),
    manager=manager
)

clock = pygame.time.Clock()
running = True
value = slider.get_current_value()

while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

    manager.update(time_delta)
    value = slider.get_current_value()  # real-time value

    screen.fill((30, 30, 30))
    manager.draw_ui(screen)
    pygame.display.update()
