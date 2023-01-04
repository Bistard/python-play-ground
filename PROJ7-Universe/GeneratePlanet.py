from pygame import draw
from math import sin, cos


class Planet:

    def __init__(self, screen, color, position, radius, angle):
        self.screen = screen
        self.position = position
        self.radius = radius
        self.color = color
        self.angle = angle

    def generate_planet(self, direction, curve):
        x = int(cos(self.angle)*curve[0]+self.position[0])
        y = int(sin(self.angle)*curve[1]+self.position[1])
        if direction == 'clockwise':
            draw.circle(self.screen, self.color, (x, y), self.radius)
            return x, y
        elif direction == 'anticlockwise':
            pass
            return x, y
        elif direction == 'stop':
            draw.circle(self.screen, self.color, self.position, self.radius)
