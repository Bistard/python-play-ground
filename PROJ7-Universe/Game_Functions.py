from pygame import event, font, QUIT, draw
import sys
from settings import settings
from random import randint, uniform

uni_settings = settings()
center = [uni_settings.screen_size[0]//2, uni_settings.screen_size[1]//2]


def check_events():
    for Event in event.get():
        if Event.type == QUIT:
            sys.exit()


def text_objects(text, font, color):
    textsurface = font.render(text, True, color)
    return textsurface.get_rect()


def text_display(window, text, coors, size, color):
    largetext = font.Font('freesansbold.ttf', size)
    textsurf, textrect = text_objects(text, largetext, color)
    textrect.center = (coors)
    window.blit(textsurf, textrect)


def orbit(screen):
    radius = 50
    for i in range(0, 8):
        draw.circle(screen, uni_settings.orbit, center, radius, 1)
        radius += 50


def generate_stellar():

    num_stellar = randint(1, 1)

    with open('data.txt', 'w') as data:
        for i in range(0, num_stellar):
            # names
            data.write('P')
            for ii in range(0, 5):
                data.write(str(randint(0, 9)))
            data.write(',')
            # colors
            color = [0, 0, 0]
            for ii in range(0, 3):
                num = randint(0, 255)
                if num < 100:
                    num = '0'+str(num)
                    if int(num) < 10:
                        num = '0'+str(num)
                else:
                    num = str(num)
                color[ii] = num
            data.write(str(color))
            data.write(',')
            # positions
            if num_stellar == 1:
                position = uni_settings.screen_size[0] // 2, uni_settings.screen_size[1] // 2
                data.write(str(position))
            elif num_stellar == 2:
                if i == 0:
                    position = (uni_settings.screen_size[0] // 2) - 80, uni_settings.screen_size[1] // 2
                    data.write(str(position))
                elif i == 1:
                    position = (uni_settings.screen_size[0] // 2) + 80, uni_settings.screen_size[1] // 2
                    data.write(str(position))
            elif num_stellar == 3:
                if i == 0:
                    position = (uni_settings.screen_size[0] // 2) - 80, (uni_settings.screen_size[1] // 2) + 80
                    data.write(str(position))
                elif i == 1:
                    position = (uni_settings.screen_size[0] // 2) + 80, (uni_settings.screen_size[1] // 2) + 80
                    data.write(str(position))
                elif i == 2:
                    position = uni_settings.screen_size[0] // 2, (uni_settings.screen_size[1] // 2) - 80
                    data.write(str(position))
            data.write(',')
            # radius
            data.write(str(randint(35, 75)))
            data.write(',')
            # change
            change = str(round(uniform(0.0005, 0.003), 5))
            while len(change) < 7:
                change = change + '0'
            data.write(change)
            data.write(',')
            # angle
            data.write('0')
            data.write('\n')
    return num_stellar


def generate_planet():

    num_planet = randint(1, 4)

    with open('planet_data.txt', 'w') as data:
        for i in range(0, num_planet):
            # names
            data.write('P')
            for ii in range(0, 5):
                data.write(str(randint(0, 9)))
            data.write(',')
            # colors
            color = [0, 0, 0]
            for ii in range(0, 3):
                num = randint(0, 255)
                if num < 100:
                    num = '0'+str(num)
                    if int(num) < 10:
                        num = '0'+str(num)
                else:
                    num = str(num)
                color[ii] = num
            data.write(str(color))
            data.write(',')
            # radius
            radius = str(randint(1, 25))
            if len(radius) < 2:
                radius = '0' + radius
            data.write(radius)
            data.write(',')
            # change
            change = str(round(uniform(0.0001, 0.003), 5))
            while len(change) < 7:
                change = change + '0'
            data.write(change)
            data.write(',')
            # angle
            data.write('0')
            data.write('\n')
    return num_planet
