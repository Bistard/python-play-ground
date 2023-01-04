# Tetris
import pygame
import math
import random
import time

pygame.init()
# basic color
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREY = [50,50,50]
LIGHTGREY = [100,100,100]
# colors for each different tetris
LIGHTBLUE = [108,255,255]
ORANGE = [255,173,91]
BLUE = [4,180,255]
YELLOW = [255,242,9]
RED = [241,78,86]
GREEN = [181,230,29]
PURPLE = [179,83,179]

score = [0]
window_width, window_height = 750, 950
clock = pygame.time.Clock()
background = pygame.image.load('background.png')
menu = pygame.image.load('menu.png')
STATS = pygame.image.load('STATS.png')
gameover = pygame.image.load('GameOver.png')
# pictures of each different tetris & transform them into the same sizes
Ii = pygame.image.load('tetrises/Ii.jpg')
Ii = pygame.transform.scale(Ii,(20,80))
Jj = pygame.image.load('tetrises/Jj.png')
Jj = pygame.transform.scale(Jj,(40,60))
Ll = pygame.image.load('tetrises/Ll.png')
Ll = pygame.transform.scale(Ll,(40,60))
Oo = pygame.image.load('tetrises/Oo.jpg')
Oo = pygame.transform.scale(Oo,(40,40))
Ss = pygame.image.load('tetrises/Ss.png')
Ss = pygame.transform.scale(Ss,(40,60))
Tt = pygame.image.load('tetrises/Tt.png')
Tt = pygame.transform.scale(Tt,(60,40))
Zz = pygame.image.load('tetrises/Zz.png')
Zz = pygame.transform.scale(Zz,(40,60))
SPACE = pygame.image.load('samples/SPACE.jpg')
SPACE = pygame.transform.scale(SPACE,(80,30))
W = pygame.image.load('samples/W.jpg')
W = pygame.transform.scale(W,(30,30))
A = pygame.image.load('samples/A.jpg')
A = pygame.transform.scale(A,(30,30))
S = pygame.image.load('samples/S.jpg')
S = pygame.transform.scale(S,(30,30))
D = pygame.image.load('samples/D.jpg')
D = pygame.transform.scale(D,(30,30))
#display texts


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def text_display(window, text, size, coordinate, color):
    large_text = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = coordinate
    window.blit(text_surf, text_rect)


# create & display a button with any texts inside
def button(window,color,coors,size,text,textsize,textcolor):
    pygame.draw.rect(window,color,(coors,size))
    pygame.draw.rect(window,WHITE,(coors,size),3)
    text_display(window,text,textsize,(coors[0]+math.floor(size[0]/2),coors[1]+math.floor(size[1]/2)),textcolor)
#menu window
def startmenu():
    mainwindow = pygame.display.set_mode((window_width, window_height))
    textsize = 30
    while True:
        # gets mouse input
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mainwindow.blit(menu,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        # All these are UI buttons
        if 235 < mouse[0] < 415 and 500 < mouse[1] < 550:
            GO = button(mainwindow,LIGHTGREY,(235,500),(180,50),'GO',textsize,WHITE)
            if click[0] == 1:
                return 'Go'
        else:
            GO = button(mainwindow,GREY,(235,500),(180,50),'GO',30,WHITE)

        if 335 < mouse[0] < 515 and 580 < mouse[1] < 660:
            STATS = button(mainwindow,LIGHTGREY,(335,580),(180,50),'STATS',textsize,WHITE)
            if click[0] == 1:
                return 'Stats'
        else:
            STATS = button(mainwindow,GREY,(335,580),(180,50),'STATS',textsize,WHITE)
        
        if 235 < mouse[0] < 415 and 660 < mouse[1] < 740:
            TUTORIAL = button(mainwindow,LIGHTGREY,(235,660),(180,50),'TUTORIAL',textsize,WHITE)
            if click[0] == 1:
                mainwindow.blit(SPACE,(135,680))
                mainwindow.blit(W,(60,645))
                mainwindow.blit(A,(25,680))
                mainwindow.blit(S,(60,680))
                mainwindow.blit(D,(95,680))
        else:
            TUTORIAL = button(mainwindow,GREY,(235,660),(180,50),'TUTORIAL',textsize,WHITE)
        
        if 335 < mouse[0] < 515 and 740 < mouse[1] < 820:
            EXIT = button(mainwindow,LIGHTGREY,(335,740),(180,50),'EXIT',textsize,WHITE)
            if click[0] == 1:
                return 'Exit'
        else:
            EXIT = button(mainwindow,GREY,(335,740),(180,50),'EXIT',textsize,WHITE)

        pygame.display.update()
        clock.tick(60)
#stats window
def stats():
    mainwindow = pygame.display.set_mode((window_width, window_height))
    while True:
        textsize = 20
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mainwindow.blit(STATS,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        # Read 2 files and print stats on the screen 
        with open('RecentStats.asd', 'r') as recent:
            coors = [200,400]
            for line in recent.readlines(): 
                line = line.strip('\n')
                text_display(mainwindow,line,textsize,coors,WHITE)
                coors[1] += 50
        with open('TotalStats.asd','r') as total:
            coors = [560,400]
            for line in total.readlines():
                line = line.strip('\n')
                text_display(mainwindow,line,textsize,(coors[0],coors[1]),WHITE)
                coors[1] += 50
        # UI buttons
        text_display(mainwindow,'Recent',60,(200,350),WHITE)
        text_display(mainwindow,'Total',60,(560,350),WHITE)
        if 20 < mouse[0] < 100 and 880 < mouse[1] < 920:
            button(mainwindow,LIGHTGREY,(20,880),(80,40),'BACK',20,WHITE)
            if click[0] == 1:
                return
        else:
            button(mainwindow,GREY,(20,880),(80,40),'BACK',20,WHITE)
        pygame.display.update()
        clock.tick(60)
#gaming window
def mainloop():
    mainwindow = pygame.display.set_mode((window_width, window_height))
    # All 7 different tetrises and each one have 4 different states 
    def I(state):
        if state == 0:
            for i in range(0,4):
                updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                updatec_zone()
        if state == 1:
            for i in range(0,4):
                updatecoors(i,[LRD[2][0]+2,i+LRD[0][0]-1])
                updatec_zone()
        if state == 2:
            for i in range(0,4):
                updatecoors(i,[i+LRD[2][0]+1,LRD[0][0]])
                updatec_zone()
        if state == 3:
            for i in range(0,4):
                updatecoors(i,[LRD[2][0]+2,i+LRD[0][0]-2])
                updatec_zone()
    def L(state):
        if state == 0:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                if i == 3:
                    updatecoors(i,[LRD[2][0]+2,LRD[0][0]+1])
                updatec_zone()
        if state == 1:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]+1-i])
                if i == 3:
                    updatecoors(i,[LRD[2][0]+2,LRD[0][0]-1])
                updatec_zone()
        if state == 2:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                if i == 3:
                    updatecoors(i,[LRD[2][0],LRD[0][0]-1])
                updatec_zone()
        if state == 3:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]-1+i])
                if i == 3:
                    updatecoors(i,[LRD[2][0],LRD[0][0]+1])
                updatec_zone()
    def J(state):
        if state == 0:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                if i == 3:
                    updatecoors(i,[LRD[2][0]+2,LRD[0][0]-1])
                updatec_zone()
        if state == 1:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]+1-i])
                if i == 3:
                    updatecoors(i,[LRD[2][0],LRD[0][0]-1])
                updatec_zone()
        if state == 2:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                if i == 3:
                    updatecoors(i,[LRD[2][0],LRD[0][0]+1])
                updatec_zone()
        if state == 3:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]-1+i])
                if i == 3:
                    updatecoors(i,[LRD[2][0]+2,LRD[0][0]+1])
                updatec_zone()
    def O(state):
        for i in range(0,4):
            if i < 2:
                updatecoors(i,[LRD[2][0],LRD[0][0]+i])
            elif i >= 2:
                updatecoors(i,[LRD[2][0]+1,LRD[0][0]-2+i])
            updatec_zone()
    def Z(state):
        if state == 0:
            for i in range(0,4):
                if i < 2:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                elif i >= 2:
                    updatecoors(i,[i+LRD[2][0]-1,LRD[0][0]-1])
                updatec_zone()
        if state == 1:
            for i in range(0,4):
                if i < 2:
                    updatecoors(i,[LRD[2][0],LRD[0][0]-1+i])
                elif i >= 2:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]-2+i])
                updatec_zone()
        if state == 2:
            for i in range(0,4):
                if i < 2:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]+1])
                elif i >= 2:
                    updatecoors(i,[i+LRD[2][0]-1,LRD[0][0]])
                updatec_zone()
        if state == 3:
            for i in range(0,4):
                if i < 2:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]-1+i])
                elif i >= 2:
                    updatecoors(i,[LRD[2][0]+2,LRD[0][0]-2+i])
                updatec_zone()
    def S(state):
        if state == 0:
            for i in range(0,4):
                if i < 2:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                elif i >= 2:
                    updatecoors(i,[i+LRD[2][0]-1,LRD[0][0]+1])
                updatec_zone()
        if state == 1:
            for i in range(0,4):
                if i < 2:
                    updatecoors(i,[LRD[2][0],LRD[0][0]+2-i])
                elif i >= 2:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]+3-i])
                updatec_zone()
        if state == 2:
            for i in range(0,4):
                if i < 2:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]+1])
                elif i >= 2:
                    updatecoors(i,[i+LRD[2][0]-1,LRD[0][0]+2])
                updatec_zone()
        if state == 3:
            for i in range(0,4):
                if i < 2:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]+2-i])
                elif i >= 2:
                    updatecoors(i,[LRD[2][0]+2,LRD[0][0]+3-i])
                updatec_zone()
    def T(state):
        if state == 0:
            for i in range(0,4):
                if i < 1:
                    updatecoors(i,[LRD[2][0],LRD[0][0]])
                elif i >= 1:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]-2+i])
                updatec_zone()
        if state == 1:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                elif i == 3:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]+1])
                updatec_zone()
        if state == 2:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]-1+i])
                elif i == 3:
                    updatecoors(i,[LRD[2][0]+2,LRD[0][0]])
                updatec_zone()
        if state == 3:
            for i in range(0,4):
                if i < 3:
                    updatecoors(i,[i+LRD[2][0],LRD[0][0]])
                if i == 3:
                    updatecoors(i,[LRD[2][0]+1,LRD[0][0]-1])
                updatec_zone()
    QUIT = False
    # these are using for recording stats
    line_cleared = [0]
    Singles = [0]
    Doubles = [0]
    Triples = [0]
    Tetrises = [0]
    # 'count' = frame
    count = 0
    coors_tetris = []
    states = []
    shapes = []
    shapes_pics = [Ii,Ll,Jj,Oo,Zz,Ss,Tt]
    # it will add a relative coordinates into this 'zone' for stale tetris which you are not holding
    zone = [[8,0,0,0,0,0,0,0,0,0,0,8],   # 12x21
            [8,0,0,0,0,0,0,0,0,0,0,8],   # 0 meaning nothing there
            [8,0,0,0,0,0,0,0,0,0,0,8],   # 8 meaning there is a invisible wall
            [8,0,0,0,0,0,0,0,0,0,0,8],   
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,0,0,0,0,0,0,0,0,0,0,8],
            [8,8,8,8,8,8,8,8,8,8,8,8]]
    # This zone add a relative coordinates for current tetris you are holding and update every single frame
    c_zone = [[8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],    
              [8,0,0,0,0,0,0,0,0,0,0,8],    
              [8,0,0,0,0,0,0,0,0,0,0,8],     
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,0,0,0,0,0,0,0,0,0,0,8],
              [8,8,8,8,8,8,8,8,8,8,8,8]]
    # determine COLLIDE OR NOT
    TOUCH = [True]
    # copy the whole 'zone' into 'c_zone'
    def updatec_zone():
        c_zone.clear()
        for i in range(0,22):
            c_zone.append(zone[i].copy())
    # Once you touch something, add 1~7 numbers into 'zone' which means each different tetris
    def updatezone(zone,i,shape):
        if shape == 0:
            zone[coors_tetris[i][0]-1][coors_tetris[i][1]] = 1
        if shape == 1:
            zone[coors_tetris[i][0]-1][coors_tetris[i][1]] = 2
        if shape == 2:
            zone[coors_tetris[i][0]-1][coors_tetris[i][1]] = 3
        if shape == 3:
            zone[coors_tetris[i][0]-1][coors_tetris[i][1]] = 4
        if shape == 4:
            zone[coors_tetris[i][0]-1][coors_tetris[i][1]] = 5
        if shape == 5:
            zone[coors_tetris[i][0]-1][coors_tetris[i][1]] = 6
        if shape == 6:
            zone[coors_tetris[i][0]-1][coors_tetris[i][1]] = 7
    # those 2 are for the testing
    def printzone():
        for i in range(0,22):
            print(zone[i])
        print('------------------------------')
    def printc_zone():
        for i in range(0,22):
            print(c_zone[i])
        print('------------------------------')
    # draw the grid
    def updategrid(window_x,window_y,color,width):
        gw_width = 400
        gw_height = 800
        side = 40
        yy = window_y
        for i in range(0,math.floor(gw_height/side)):
            xx = window_x
            for ii in range(0,math.floor(gw_width/side)):
                pygame.draw.rect(mainwindow,color,(xx,yy,41,41),width)
                xx += 40
            yy += 40
    # according to the 'c_zone' draw the real game zone
    def updatetetris():
        y = 60
        for i in range(0,21):
            x = 160
            for ii in range(1,11):
                if i == 0:
                    break
                if c_zone[i][ii] == 0:
                    pygame.draw.rect(mainwindow,GREY,(x,y,41,41))
                if c_zone[i][ii] == 1:
                    pygame.draw.rect(mainwindow,LIGHTBLUE,(x,y,41,41))
                if c_zone[i][ii] == 2:
                    pygame.draw.rect(mainwindow,ORANGE,(x,y,41,41))
                if c_zone[i][ii] == 3:
                    pygame.draw.rect(mainwindow,BLUE,(x,y,41,41))
                if c_zone[i][ii] == 4:
                    pygame.draw.rect(mainwindow,YELLOW,(x,y,41,41))
                if c_zone[i][ii] == 5:
                    pygame.draw.rect(mainwindow,RED,(x,y,41,41))
                if c_zone[i][ii] == 6:
                    pygame.draw.rect(mainwindow,GREEN,(x,y,41,41))
                if c_zone[i][ii] == 7:
                    pygame.draw.rect(mainwindow,PURPLE,(x,y,41,41))
                x += 40
            y += 40
    # move DOWN or LEFT or RIGHT
    def moveASD(ASD):
        if ASD == 'S':
            LRD[2][0] += 1
        if ASD == 'A':
            LRD[0][0] -= 1
        elif ASD == 'D': 
            LRD[0][0] += 1
    # rotation
    def rotation():
        if states[-1] < 3:
            states[-1] += 1
        else :
            states[-1] = 0
    # shift to change another tetrimino
    def moveSHIFT(SHIFT):
        if SHIFT == 'SHIFT':
            TOUCH.append(True)
    # judge you COLLIDE or NOT ---- most important thing

    def gravity():
        for i in range(0,4):
            if c_zone[coors_tetris[i][0]][coors_tetris[i][1]] != 0:
                return True
        return False
    # add coordinates of the tetris you are holding into a list
    def updatecoors(i,coors):
        coors_tetris.append(coors)
    # moverow
    def moverow():
        count = 0
        for i in range(0,21):
            if zone[i].count(0) == 0:
                zone.remove(zone[i])
                zone.insert(0,[8,0,0,0,0,0,0,0,0,0,0,8])
                count += 1
        # scoring system & record stats
        if count == 1:
            score[0] += 100
            line_cleared[0] += 1
            Singles[0] += 1
        elif count == 2:
            score[0] += 300
            line_cleared[0] += 2
            Doubles[0] += 1
        elif count == 3:
            score[0] += 600
            line_cleared[0] += 3
            Triples[0] += 1
        elif count == 4:
            score[0] += 1000
            line_cleared[0] += 4
            Tetrises[0] += 1
    # 
    def g_tetrises(shape,states):
        if shape == 0:
            I(states)
        elif shape == 1:
            L(states)
        elif shape == 2:
            J(states)
        elif shape == 3:
            O(states)
        elif shape == 4:
            Z(states)
        elif shape == 5:
            S(states)
        elif shape == 6:
            T(states)
    # timing system
    start_time = time.perf_counter()
    def TIME():  
        over_time = time.perf_counter()
        used_time = over_time - start_time  
        global time_sec, time_min, time_hour  
        time_sec = int(used_time % 60)  
        time_min = int((used_time // 60) % 60)  
        time_hour = int((used_time // 60) // 60)  
    # generates first 5 tetrises
    for i in range(0,6):
        shapes.append(random.randint(0,6))
    while not QUIT:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mainwindow.blit(background,(0,0))
        count += 1
        # once there is a COLLISION generates a new tetris
        if TOUCH[-1] == True:
            count = 0
            LRD = [[6],[0],[0]]
            del(shapes[-1])
            shapes.insert(0,random.randint(0,6))
            shape = shapes[-1]
            states.append(0)
            TOUCH.append(False)

        g_tetrises(shape,states[-1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # Hard drop
                    while True:
                        g_tetrises(shape,states[-1])
                        if gravity() == False:
                            LRD[2][0] += 1
                            coors_tetris.clear()
                        elif gravity() == True:
                            for i in range(0,4):
                                updatezone(zone,i,shape)
                            break
                    TOUCH[-1] = True
                if event.key == pygame.K_w: #clockwise rotation
                    rotation()
                if event.key == pygame.K_a:
                    moveASD('A')
                if event.key == pygame.K_d:
                    moveASD('D')
                if event.key == pygame.K_s: # soft drop
                    moveASD('S')
                if event.key == pygame.K_LSHIFT:
                    moveSHIFT('SHIFT')
        # testing COLLISION
        if gravity() == True:
            TOUCH.append(True)
            for i in range(0,4):
                updatezone(zone,i,shape)
        elif gravity() == False:
            for i in range(0,4):
                updatezone(c_zone,i,shape)
        # every 1 sec drop one unit
        if count % 60 == 0:
            LRD[2][0] += 1
        moverow()
        updatetetris()
        coors_tetris.clear()
        TIME()
        # display the HOLD
        if shape == 0:
            mainwindow.blit(Ii,(660,70))
        elif shape == 1:
            mainwindow.blit(Ll,(650,80))
        elif shape == 2:
            mainwindow.blit(Jj,(650,80))
        elif shape == 3:
            mainwindow.blit(Oo,(650,90))
        elif shape == 4:
            mainwindow.blit(Zz,(650,80))
        elif shape == 5:
            mainwindow.blit(Ss,(650,80))
        elif shape == 6:
            mainwindow.blit(Tt,(640,90))
        # display the next 5 tetrises
        y = 680
        for i in shapes[0:5]:
            mainwindow.blit(shapes_pics[i],(650,y))
            y -= 100

        text_display(mainwindow,str(score[0]),30,(70,115),WHITE)
        text_display(mainwindow,str(time_hour)+':'+str(time_min)+':'+str(time_sec),30,(70,200),WHITE)
        text_display(mainwindow,'SCORE',30,(70,40),WHITE)
        text_display(mainwindow,'HOLD',30,(670,40),WHITE)
        text_display(mainwindow,'NEXT',30,(670,200),WHITE)
        if 20 < mouse[0] < 100 and 880 < mouse[1] < 920:
            button(mainwindow,LIGHTGREY,(20,880),(80,40),'BACK',20,WHITE)
            if click[0] == 1:
                return
        else:
            button(mainwindow,GREY,(20,880),(80,40),'BACK',20,WHITE)
        
        #GAME OVER & records stats
        if zone[0][6] != 0: # means gameover
            with open('RecentStats.asd', 'w+') as recent: # I didn't use '.txt' to prevent you can change stats easily outside the game
                recent.write('Score :'+str(score[0])+'\n')
                recent.write('Lines_cleared :'+str(line_cleared[0])+'\n')
                recent.write('Singles :'+str(Singles[0])+'\n')
                recent.write('Doubles :'+str(Doubles[0])+'\n')
                recent.write('Triples :'+str(Triples[0])+'\n')
                recent.write('Tetrises :'+str(Tetrises[0])+'\n')
                with open('TotalStats.asd', 'r+') as total:
                    recent.seek(0,0)
                    recent_scores = int(recent.readline()[7:])
                    recent_line_cleared = int(recent.readline()[15:])
                    recent_singles = int(recent.readline()[9:])
                    recent_doubles = int(recent.readline()[9:])
                    recent_triples = int(recent.readline()[9:])
                    recent_tetrises = int(recent.readline()[10:])
                    total.seek(0,0)
                    total_scores = int(total.readline()[15:])
                    total_line_cleared = int(total.readline()[15:])
                    total_singles = int(total.readline()[9:])
                    total_doubles = int(total.readline()[9:])
                    total_triples = int(total.readline()[9:])
                    total_tetrises = int(total.readline()[10:])
                    
                    total_line_cleared = total_line_cleared + recent_line_cleared
                    total_singles = total_singles + recent_singles
                    total_doubles = total_doubles + recent_doubles
                    total_triples = total_triples + recent_triples
                    total_tetrises = total_tetrises + recent_tetrises
                with open('TotalStats.asd','w+') as total:
                    if recent_scores > total_scores:
                        total.write('Highest score :'+str(recent_scores)+'\n')
                    else:
                        total.write('Highest score :'+str(total_scores)+'\n')
                    total.write('Lines_cleared :'+str(total_line_cleared)+'\n')
                    total.write('Singles :'+str(total_singles)+'\n')
                    total.write('Doubles :'+str(total_singles)+'\n')
                    total.write('Triples :'+str(total_triples)+'\n')
                    total.write('Tetrises :'+str(total_tetrises)+'\n')
            return 'GameOver'

        updategrid(160,100,WHITE,2)
        pygame.display.update()
        clock.tick(60)
#gameover-window
def GameOver():
    mainwindow = pygame.display.set_mode((window_width, window_height))
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mainwindow.blit(gameover,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        text_display(mainwindow,'Your Score is:  '+str(score[0]),50,(375,475),WHITE)
        if 20 < mouse[0] < 100 and 880 < mouse[1] < 920:
            button(mainwindow,LIGHTGREY,(20,880),(80,40),'BACK',20,WHITE)
            if click[0] == 1:
                return
        else:
            button(mainwindow,GREY,(20,880),(80,40),'BACK',20,WHITE)

        pygame.display.update()
        clock.tick(60)
# Actually running here
while True:
    LEVEL = startmenu()
    if LEVEL == 'Go':
        if mainloop() == 'GameOver':
            GameOver()
    elif LEVEL == 'Stats':
        stats()
    elif LEVEL == 'Exit':
        pygame.quit()
        quit()
