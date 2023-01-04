import pygame
import random


def bubble_sort(l, i):
    if len(l) == 1:
        return l
    else:
        while i != len(l) - 1:
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
            i += 1
        return bubble_sort(l[:-1], 0)+[l[-1]]


pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (180, 180, 180)
GREEN = (34, 177, 76)
BLUE = (34, 76, 177)
window_width, window_height = 1200, 800
clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height))

lists = [i for i in range(100)]
random.shuffle(lists)
steps = [lists]

if __name__ == '__main__':

    while True:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()
        clock.tick(60)
