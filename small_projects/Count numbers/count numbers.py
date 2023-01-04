import pygame
import random


def text_objects(text, font, color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def text_display(window, text, size, coors, color):
    largetext = pygame.font.Font('freesansbold.ttf', size)
    textsurf, textrect = text_objects(text, largetext, color)
    textrect.center = (coors)
    window.blit(textsurf, textrect)


pygame.init()

window_width, window_height = 800, 800
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
bar_color = [200, 200, 200]
white = [255, 255, 255]
black = [0, 0, 0]

right = 0
down = 70
bar_height = 50
gap = 15
bars = [pygame.Rect(right, down*0+gap, 0, bar_height),
        pygame.Rect(right, down*1+gap, 0, bar_height),
        pygame.Rect(right, down*2+gap, 0, bar_height),
        pygame.Rect(right, down*3+gap, 0, bar_height),
        pygame.Rect(right, down*4+gap, 0, bar_height),
        pygame.Rect(right, down*5+gap, 0, bar_height),
        pygame.Rect(right, down*6+gap, 0, bar_height),
        pygame.Rect(right, down*7+gap, 0, bar_height),
        pygame.Rect(right, down*8+gap, 0, bar_height),
        pygame.Rect(right, down*9+gap, 0, bar_height)]

random_num = []
for i in range(0, 10):
    random_num.append(0)

while True:

    rand_num = random.randint(0, 9)
    random_num[rand_num] += 1


    window.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for i in range(0, 10):
        bars[i][2] = random_num[i]

    for bar in bars:
        pygame.draw.rect(window, bar_color, [bar[0], bar[1], bar[2], bar[3]])
        text_display(window, str(int((random_num[bars.index(bar)])*2)), 30, [bar[2]+50, bar[1]+25], black)
    pygame.display.update()
    clock.tick()
