from pygame import display, init
from settings import settings
from GeneratePlanet import Planet
import Game_Functions as gf
import systems as G
from random import randint


def run_game():
    init()
    uni_settings = settings()
    screen = display.set_mode(uni_settings.screen_size)
    display.set_caption('Universe')

    while True:
        screen.fill(uni_settings.black)
        gf.check_events()

        # gf.orbit(screen)
        # G.solar_system(screen, uni_settings, uni_settings.earth_angle, uni_settings.moon_angle, uni_settings.
        #               mercury_angle, uni_settings.venus_angle,uni_settings.mars_angle, uni_settings.jupiter_angle,
        #               uni_settings.saturn_angle, uni_settings.uranus_angle, uni_settings.neptune_angle)
        # G.rotating_solar_system(uni_settings)

        for i in range(1, num_stellar + 1):
            stellar_data = G.read_data('data.txt', i)
            stellar = Planet(screen, stellar_data[1], stellar_data[2], stellar_data[3], stellar_data[5])
            temp = stellar.generate_planet('clockwise', [0, 0])
            G.rotating_random_system('data.txt', i, stellar_data[4], stellar_data[5])

        for i in range(1, num_planet + 1):
            print(i)
            planet_data = G.read_planet_data('planet_data.txt', i)
            planet = Planet(screen, planet_data[1], [temp[0], temp[1]], planet_data[3], planet_data[5])
            planet.generate_planet('clockwise', [120, 120])
            G.rotating_random_planet('planet_data.txt', i, planet_data[4], planet_data[5])
        display.flip()


num_stellar = gf.generate_stellar()
num_planet = gf.generate_planet()

run_game()

# BUGS
# 1. 多个planets的时候会referenced be fore assignment
