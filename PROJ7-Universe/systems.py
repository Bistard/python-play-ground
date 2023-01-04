from GeneratePlanet import Planet
from settings import settings

uni_settings = settings()

center = [uni_settings.screen_size[0]//2, uni_settings.screen_size[1]//2]


def solar_system(screen, uni_settings, sun_angle, moon_angle, mercury_angle, venus_angle,
                 mars_angle, jupiter_angle, saturn_angle, uranus_angle, neptune_angle):

    sun = Planet(screen, uni_settings.Sun, center, 40, sun_angle)
    sun.generate_planet('stop', [100, 100])

    earth = Planet(screen, uni_settings.Earth, center, 4, sun_angle)
    temp = earth.generate_planet('clockwise', [150, 150])

    moon = Planet(screen, uni_settings.Moon, [temp[0], temp[1]], 1, moon_angle)
    moon.generate_planet('clockwise', [10, 10])

    mercury = Planet(screen, uni_settings.Mercury, center, 2, mercury_angle)
    mercury.generate_planet('clockwise', [50, 50])

    venus = Planet(screen, uni_settings.Venus, center, 4, venus_angle)
    venus.generate_planet('clockwise', [100, 100])

    mars = Planet(screen, uni_settings.Mars, center, 3, mars_angle)
    mars.generate_planet('clockwise', [200, 200])

    jupiter = Planet(screen, uni_settings.Jupiter, center, 18, jupiter_angle)
    jupiter.generate_planet('clockwise', [250, 250])

    saturn = Planet(screen, uni_settings.Saturn, center, 15, saturn_angle)
    saturn.generate_planet('clockwise', [300, 300])

    uranus = Planet(screen, uni_settings.Uranus, center, 8, uranus_angle)
    uranus.generate_planet('clockwise', [350, 350])

    neptune = Planet(screen, uni_settings.Neptune, center, 9, neptune_angle)
    neptune.generate_planet('clockwise', [400, 400])


def rotating_solar_system(uni_settings):
    uni_settings.earth_angle += 0.001
    uni_settings.moon_angle += 0.0135
    uni_settings.mercury_angle += 0.00415
    uni_settings.venus_angle += 0.00162
    uni_settings.mars_angle += 0.00053
    uni_settings.jupiter_angle += 0.00008
    uni_settings.saturn_angle += 0.00003
    uni_settings.uranus_angle += 0.000001
    uni_settings.neptune_angle += 0.000006


def read_data(file, lines):
    stellar_color = []
    stellar_posi = []
    with open(file, 'r') as data:
        for i, line in enumerate(data):
            if i == lines-1:
                stellar_name = line[0:6]
                stellar_color.append(int(line[9:12]))
                stellar_color.append(int(line[16:19]))
                stellar_color.append(int(line[23:26]))
                stellar_posi.append(int(line[30:33]))
                stellar_posi.append(int(line[35:38]))
                stellar_rad = int(line[40:42])
                stellar_cha = float(line[43:50])
                stellar_ang = float(line[51:-1])
        return stellar_name, stellar_color, stellar_posi, stellar_rad, stellar_cha, stellar_ang


def read_planet_data(file, lines):
    planet_color = []
    with open(file, 'r') as data:
        for i, line in enumerate(data):
            if i == lines-1:
                planet_name = line[0:6]
                planet_color.append(int(line[9:12]))
                planet_color.append(int(line[16:19]))
                planet_color.append(int(line[23:26]))
                planet_rad = int(line[29:31])
                planet_cha = float(line[32:39])
                planet_ang = float(line[40:-1])
        return planet_name, planet_color, 0, planet_rad, planet_cha, planet_ang


def rotating_random_system(file, lines, stellar_ang, stellar_cha):
    with open(file, 'r') as data:
        for i, line in enumerate(data):
            if i == lines - 1:
                stellar_ang += stellar_cha
                new_line = line[:50] + ',' + str(stellar_ang)
            with open(file, 'w') as data:
                    data.write(new_line)
                    data.write('\n')


def rotating_random_planet(file, lines, stellar_ang, stellar_cha):
    with open(file, 'r') as data:
        for i, line in enumerate(data):
            if i == lines - 1:
                stellar_ang += stellar_cha
                new_line = line[:39] + ',' + str(stellar_ang)
            with open(file, 'w') as data:
                    data.write(new_line)
                    data.write('\n')
