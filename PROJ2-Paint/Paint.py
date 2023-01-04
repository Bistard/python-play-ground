import pygame
import sys
pygame.init()

BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
BLUE = [0,0,255]
GREEN = [0,255,0]
YELLOW = [230,255,0]
CYAN  = [0,255,255]
MAGENTA = [255,0,255]
GREY = [200,200,200]
colors = [RED,GREEN,BLUE,YELLOW,CYAN,MAGENTA,WHITE,BLACK]
click_color = BLACK
window_width,window_height = 1200,800
size_colors = 20,20
num_colors = 8
QUIT = False
window = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()
painting = []
passes = 0
def Palette(num):
   y_coor = []
   y = 100
   for i in range(0,num):
       y_coor.append(y)
       y += 50
   return y_coor



while not QUIT:
   window.fill(GREY)
   canvas = pygame.draw.rect(window, WHITE, (200, 50, 900, 700))
   Palette(num_colors)
   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_pressed()

   for i in range(0,num_colors):
       if 50 < mouse[0] < 70 and Palette(num_colors)[i] < mouse[1] < Palette(num_colors)[i]+20:
           if click[0] == 1:
               click_color = colors[i-1]
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()
       if event.type == pygame.MOUSEBUTTONDOWN:
           passes += 1
           painting.append([click_color])
       if event.type == pygame.MOUSEBUTTONUP:
           pass
   if click[0] == 1:
       if 200 < mouse[0] < 900 + 200 and 50 < mouse[1] < 700 + 50:
           painting[passes-1].append(mouse)

   if passes >=1 :
       for ii in painting:
           for i in range(2,len(ii)):
               try:
                   #pygame.draw.aalines(window,ii[0], True, (ii[i - 1], ii[i]),1)
                   pygame.draw.lines(window,ii[0], True, (ii[i - 1], ii[i]),3)
               except:
                   pass

   for i in range(0,num_colors):
       pygame.draw.rect(window,colors[i-1],(50,Palette(num_colors)[i],20,20))

   pygame.draw.circle(window,BLACK,(60,600),15)
   if 45 < mouse[0] < 75 and 585 < mouse[1] < 615:
       if click[0] == 1:
           painting = []
           passes = 0

   pygame.display.update()
   clock.tick()

