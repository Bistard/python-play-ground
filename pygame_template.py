import pygame

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]
YELLOW = [255, 255, 0]
PINK = [255, 120, 193]
ORANGE = [255, 165, 0]
MAGENTA = [255, 0, 255]

window_width, window_height = 1200, 800


clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height))


while True:

    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
    clock.tick(60)
