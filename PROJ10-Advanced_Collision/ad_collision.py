import random
import math
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
player_colors = [YELLOW, MAGENTA, PINK, ORANGE]
bot_colors = [BLUE, GREEN, WHITE, RED]

circles = []
player_r = 20, 50
player_v = 1, 5
window_width, window_height = 1200, 800


clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height))


class Player:

    def __init__(self, color, name):
        self.name = name
        self.color = color
        self.r = random.randint(player_r[0], player_r[1])
        self.x, self.y = random.randint(0+self.r, window_width-self.r), random.randint(0+self.r, window_height-self.r)
        self.v_x, self.v_y = random.randint(player_v[0], player_v[1]), random.randint(player_v[0], player_v[1])

    def draw(self):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.r)
        pygame.draw.circle(window, BLACK, [self.x, self.y], self.r, 1)

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

    def detect_wall(self):
        if self.x-self.r < 0 or self.x+self.r > window_width:
            self.v_x *= -1
        elif self.y-self.r < 0 or self.y+self.r > window_height:
            self.v_y *= -1

    def detect_player(self):
        for circle in circles:
            if circle.color == self.color:
                continue
            if circle.name == 'bot' and math.sqrt(abs(self.x-circle.x)**2+abs(self.y-circle.y)**2) < self.r+circle.r:
                if circle.color == RED:
                    self.color = RED
                elif circle.color == GREEN:
                    self.color = GREEN
                elif circle.color == BLUE and self.color == GREEN:
                    self.color = BLUE
                elif circle.color == WHITE and self.color == BLUE:
                    self.v_x, self.v_y = 0, 0
                    for i in circles:
                        i.v_y, i.v_x = 0, 0


class Bot(Player):
    def __init__(self, color, name):
        super().__init__(color, name)
        if self.color == RED:
            self.x, self.y, self.r = window_width//2, window_height//2, 25
        else:
            self.r = 100
        if self.color == BLUE:
            self.x, self.y = 200, 600
        if self.color == GREEN:
            self.x, self.y = 1000, 600
        if self.color == WHITE:
            self.x, self.y = 600, 150


for i in range(0, len(player_colors)):
    circles.append(Player(player_colors[i], 'player'))
    circles.append(Bot(bot_colors[i], 'bot'))

while True:

    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for circle in circles:
        circle.draw()
        if circle.name == 'player':
            circle.detect_wall()
            circle.detect_player()
            circle.move()

    pygame.display.update()
    clock.tick(60)
