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
CYAN = [0, 255, 255]
MAGENTA = [255, 0, 255]
GREY = [200, 200, 200]
colors = [BLACK, RED, BLUE, GREEN, YELLOW, CYAN, MAGENTA, GREY]
clock = pygame.time.Clock()
window_width, window_height = 1200, 800

#These two functions in order to let me create texts easily
def text_objects(text,font,color):
   textsurface = font.render(text,True,color)
   return textsurface, textsurface.get_rect()

def text_display(window,text,size,coor_x,coor_y,color):
   largetext = pygame.font.Font('freesansbold.ttf',size)
   textsurf,textrect = text_objects(text,largetext,color)
   textrect.center = ((coor_x,coor_y))
   window.blit(textsurf,textrect)

def distance(pos1, pos2):
   return math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)

#GameWindow 
def mainloop():
   radius = []
   ball_x = []
   ball_y = []
   ball_v = []
   ball_color = [] 
   balls = []
   count = 1
   TIME = 0
   num_balls = 1
   radius_mouse_circle = 20
   QUIT = False
   window = pygame.display.set_mode((window_width, window_height))

   #Randomly generates data
   def generate_ball(num):
       for i in range(0, num):
           radius.append(random.randint(30,50))
           ball_x.append(random.randint(radius[i], window_width - radius[i]))
           ball_y.append(random.randint(radius[i], window_height - radius[i]))
           ball_v.append([random.randint(-7,7), random.randint(-7,7)])
           ball_color.append((random.choice(colors)))
           #naming each ball
           if balls.count('ball'+str(i)) == 0:
               balls.append('ball'+str(i))
           
   #Generates data
   generate_ball(num_balls)
   while not QUIT:
       #Get the position of mouse in [x,y] 
       mouse = pygame.mouse.get_pos()
       window.fill(WHITE)
       count += 1
       #Every 1 sec 'Time' plus 1
       if count%60 == 0:
           TIME += 1
       #Every 10 sec generates a new ball
       if count % 600 == 0:
           generate_ball(1)
           num_balls += 1

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               quit()
       
       #Testing the distance between each ball and if collision happens
       for i in range(0,num_balls):
           for ii in range(i,num_balls):
               try:
                   if distance(balls[i],balls[ii]) <= radius[i]+radius[ii]:
                       ball_v[i][0] = -ball_v[i][0]
                       ball_v[i][1] = -ball_v[i][1]
                       ball_v[ii][0] = -ball_v[ii][0]
                       ball_v[ii][1] = -ball_v[ii][1]
               except:
                   ii -= 1
       #Every 5 sec the velocities of balls will increase by 1 unit
       for i in range(0, num_balls):
           if count % 300 == 0:
               if ball_v[i][0] > 0:
                   ball_v[i][0] += 1
               if ball_v[i][0] < 0:
                   ball_v[i][0] -= 1
               if ball_v[i][1] > 0:
                   ball_v[i][1] += 1
               if ball_v[i][0] < 0:
                   ball_v[i][1] -= 1
           ball_x[i] += ball_v[i][0]
           ball_y[i] += ball_v[i][1]

           balls[i] = pygame.draw.circle(window, ball_color[i], (ball_x[i], ball_y[i]), radius[i])
           pygame.draw.circle(window, BLACK, (mouse), radius_mouse_circle)

           #Collisions with walls(prevent balls cross the walls)
           if balls[i].right >= window_width:
               ball_v[i][0] = -ball_v[i][0]
               ball_x[i] = window_width - radius[i]
           if balls[i].left <= 0:
               ball_v[i][0] = -ball_v[i][0]
               ball_x[i] = radius[i]
           if balls[i].bottom >= window_height:
               ball_v[i][1] = -ball_v[i][1]
               ball_y[i] = window_height - radius[i]
           if balls[i].top <= 0:
               ball_v[i][1] = -ball_v[i][1]
               ball_y[i] = radius[i]
           
           #If mouse and balls touched then game over
           if distance(mouse,[ball_x[i],ball_y[i]]) <= radius_mouse_circle+radius[i]:
               QUIT = True

       text_display(window,'Time:'+str(TIME), 30, window_width / 2, 50, BLACK)
       pygame.display.update()
       clock.tick(60)

#excute game
mainloop()


pygame.quit()
quit()
