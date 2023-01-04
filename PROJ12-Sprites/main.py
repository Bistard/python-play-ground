import pygame


class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    def load(self, filename, width, height, columns, coor):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = coor[0], coor[1], width, height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=70):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame


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
coors = [0, 400]

window_width, window_height = 1200, 800


clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height))
background = pygame.image.load('desktop.png')

people = MySprite(window)
people.load('Untitled.png', 15, 16, 5, coors)

sprite_group = pygame.sprite.Group()
sprite_group.add(people)

speed = 2

while True:

    window.fill((157, 142, 135))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    key = pygame.key.get_pressed()
    if any([key[pygame.K_RIGHT], key[pygame.K_LEFT], key[pygame.K_UP], key[pygame.K_DOWN]]):
        people.load('Untitled.png', 15, 16, 5, coors)
        if key[pygame.K_RIGHT]:
            coors[0] += speed
        if key[pygame.K_LEFT]:
            coors[0] -= speed
        if key[pygame.K_UP]:
            coors[1] -= speed
        if key[pygame.K_DOWN]:
            coors[1] += speed
    ticks = pygame.time.get_ticks()

    sprite_group.update(ticks)
    sprite_group.draw(window)

    pygame.display.update()
    clock.tick(60)
