import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
size = width, height = 1000, 600
BLUE = (0, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 100)
WHITE = (255,255,255)
GREY = (100,100,100)
pygame.mixer.music.load('BGM3.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
#游戏开始画面
def game_intro():
    game = True
    intro = pygame.display.set_mode((width,height))
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                quit()
                return game        
        window.fill(BLACK)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text_display(intro,'Version:0.2.13',12,950,590,GREY)
        text_display(intro,'FREY',100,width/3,height/2.5,WHITE)
        if width/1.3-40 < mouse[0] < width/1.3+50 and height/1.7-30 < mouse[1] < height/1.7+10:
            text_display(intro,'Play',40,width/1.3,height/1.7,WHITE)
            if click[0] == 1:
                return  game
        else:
            text_display(intro,'Play',30,width/1.3,height/1.7,WHITE)
        if width/1.3-40 < mouse[0] < width/1.3+50 and height/1.4-30 < mouse[1] < height/1.4+10:
            text_display(intro,'Exit',40,width/1.3,height/1.4,WHITE)
            if click[0] == 1:
                pygame.quit()
                quit()
                game = False
        else:
            text_display(intro,'Exit',30,width/1.3,height/1.4,WHITE)
        clock.tick(60)
        pygame.display.update()
#游戏选择画面
def game_window_opt():
    x=5
    player1 = 1
    player2 = 0
    blank1 = 1
    blank2 = 1
    time_L = 0
    rounds = ['0','1','2','3','4','5','6','7','8','9','10']
    blank1_type = 10,150
    blank2_type = 10,150
    window_opt = pygame.display.set_mode(size)
    opt = True
    while opt:
        window.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                opt = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return x , blank1_type , blank2_type , player1 , player2
                if blank2 > 0:
                    if event.key == pygame.K_LEFT:
                        blank2 = blank2 - 1
                if blank2 < 2:
                    if event.key == pygame.K_RIGHT:
                        blank2 = blank2 + 1
                if blank1 > 0:
                    if event.key == pygame.K_a:
                        blank1 = blank1 - 1
                if blank1 < 2:
                    if event.key == pygame.K_d:
                        blank1 = blank1 + 1
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(window_opt,GREY,(480,40,40,40))
        #左边3个不同板子和选项按钮%PLAYER BUTTON
        if player1 ==1:
            if 105 < mouse[0] < 122 and 85 < mouse[1] < 107:
                pygame.draw.polygon(window_opt,WHITE,[(100,97),(120,82),(120,112)])
                if click[0] == 1:
                    player1 -= 1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(105,97),(120,87),(120,107)])
        else:
            if 305 < mouse[0] < 320 and 85 < mouse[1] < 105:
                pygame.draw.polygon(window_opt,WHITE,[(325,97),(305,82),(305,112)])
                if click[0] == 1:
                    player1 += 1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(320,97),(305,87),(305,107)])
        if player1 == 1:
            text_display(window_opt,'PLAYER1',30,200,100,BLUE)
        else:
            text_display(window_opt,'COMPUTER1',30,200,100,BLUE)
        if blank1 == 2:
            pygame.draw.rect(window_opt,BLUE,(180,160,10,200))
            blank1_type = 10,200
        if blank1 == 1:
            pygame.draw.rect(window_opt,BLUE,(180,180,10,150))
            black1_type = 10,150
        if blank1 == 0:
            pygame.draw.rect(window_opt,BLUE,(180,200,10,100))
            blank1_type = 10,100
        if blank1 > 0:
            if 140 < mouse[0] < 160 and 240 < mouse[1] < 260 :
                pygame.draw.polygon(window_opt,WHITE,[(135,250),(160,237),(160,263)])
                if  click[0] == 1:
                    time_L += 2
                    if time_L % 11 == 0:
                        blank1 = blank1 - 1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(140,250),(160,240),(160,260)])
        if blank1 < 2:
            if 210 < mouse[0] < 230 and 240 < mouse[1] < 260:
                pygame.draw.polygon(window_opt,WHITE,[(235,250),(210,237),(210,263)])
                if  click[0] == 1:
                    time_L += 2
                    if time_L % 11 == 0:
                        blank1 = blank1 + 1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(230,250),(210,240),(210,260)])
        #右边3个不同板子和选项按钮%PLAYER BUTTON
        if player2 ==1:
            if 705 < mouse[0] < 722 and 85 < mouse[1] < 107:
                pygame.draw.polygon(window_opt,WHITE,[(700,97),(720,82),(720,112)])
                if click[0] == 1:
                    player2 -= 1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(705,97),(720,87),(720,107)])
        else:
            if 905 < mouse[0] < 920 and 85 < mouse[1] < 105:
                pygame.draw.polygon(window_opt,WHITE,[(925,97),(905,82),(905,112)])
                if click[0] == 1:
                    player2 += 1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(920,97),(905,87),(905,107)])
        if player2 == 1:
            text_display(window_opt,'PLAYER2',30,800,100,RED)
        else:
            text_display(window_opt,'COMPUTER2',30,800,100,RED)
        if blank2 == 2:
            pygame.draw.rect(window_opt,RED,(810,160,10,200))
            blank2_type = 10,200
        if blank2 == 1:
            pygame.draw.rect(window_opt,RED,(810,180,10,150))
            black2_type = 10,150
        if blank2 == 0:
            pygame.draw.rect(window_opt,RED,(810,200,10,100))
            blank2_type = 10,100
        if blank2 > 0:
            if 770 < mouse[0] < 790 and 240 < mouse[1] < 260 :
                pygame.draw.polygon(window_opt,WHITE,[(765,250),(790,237),(790,263)])
                if  click[0] == 1:
                    time_L += 2
                    if time_L % 11 == 0:
                        blank2 = blank2 - 1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(770,250),(790,240),(790,260)])
        if blank2 < 2:
            if 840 < mouse[0] < 860 and 240 < mouse[1] < 260:
                pygame.draw.polygon(window_opt,WHITE,[(865,250),(840,237),(840,263)])
                if  click[0] == 1:
                    time_L += 2
                    if time_L % 11 == 0:
                        blank2 = blank2 + 1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(860,250),(840,240),(840,260)])
        text_display(window_opt,rounds[x],30,500,60,WHITE)
        text_display(window_opt,'ROUNDS',22,580,60,WHITE)
        #G0
        pygame.draw.rect(window_opt,GREY,(450,500,100,50))
        if 460 < mouse[0] < 550 and 500 < mouse[1] <550:
            pygame.draw.rect(window_opt,(150,150,150),(450,500,100,50))
            text_display(window_opt,'GO!',40,500,530,WHITE)
            if click[0] == 1:
                return x , blank1_type , blank2_type ,player1 , player2
        else:
            text_display(window_opt,'GO!',40,500,530,WHITE)
        if x < 10:
            if 485 < mouse[0] < 515 and 15 < mouse[1] < 30:
                pygame.draw.polygon(window_opt,WHITE,[(500,15),(485,30),(515,30)])
                if click[0] == 1:
                    time_L += 2
                    if time_L % 11 == 0:
                        x=x+1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(500,20),(490,30),(510,30)])
        if x > 1:
            if 485 < mouse[0] < 515 and 85 < mouse[1] < 105:
                pygame.draw.polygon(window_opt,WHITE,[(500,105),(485,90),(515,90)])
                if click[0] == 1:
                    time_L += 2
                    if time_L % 11 == 0:
                        x=x-1
            else:
                pygame.draw.polygon(window_opt,WHITE,[(500,100),(490,90),(510,90)])
        pygame.display.update()
        clock.tick(60)
#文本
def text_objects(text,font,color):
    textsurface = font.render(text,True,color)
    return textsurface, textsurface.get_rect()


def text_display(window, text, size, coor_x, coor_y, color):
    largetext = pygame.font.Font('freesansbold.ttf', size)
    textsurf,textrect = text_objects(text, largetext, color)
    textrect.center = ((coor_x, coor_y))
    window.blit(textsurf,textrect)
#板子
def blank1(color,blank1_x,blank1_y,type,type1):
    blank1 = pygame.draw.rect(window, color, (blank1_x, blank1_y,type,type1))
def blank2(color,blank2_x,blank2_y,type,type1):
    blank2 = pygame.draw.rect(window, color, (blank2_x, blank2_y,type,type1))
window = pygame.display.set_mode(size)
pygame.display.set_caption("FREY")
swarm = pygame.image.load("swarm.jpg")
background = pygame.image.load('background.jpg')
#游戏主画面
def  game_loop():
    RUNNING = True
    scoreplayer_list = [0,0]
    GAME_WINDOW_OPT = game_window_opt()
    rounds = GAME_WINDOW_OPT[0]
    blank1_type = GAME_WINDOW_OPT[1]
    blank2_type = GAME_WINDOW_OPT[2]
    blanks1 = False
    blanks2 = False
    blanks3 = False
    blanks_data =[]
    Time_c = 0
    WINNER1_C = -1
    WINNER2_C = -1
    WINNER1 = -1
    WINNER2 = -1
    STARTPLAYER = random.randint(1,2)
    while RUNNING == True:
        GAME = 1
        while GAME == 1:
            rect1 = swarm.get_rect()
            blank1_height = 10
            blank1_width = 150
            blank1_x = 30
            blank1_y = 225
            blank1y_change = 0
            blank2_x = 960
            blank2_y = 225
            still = True
            move = True
            blank2y_change = 0
            speed = [5,5]
            TIME = 0
            quit = False
            scoreplayer1 = scoreplayer_list[1]
            scoreplayer2 = scoreplayer_list[0]
            if WINNER1_C != WINNER1:
                STARTPLAYER = 1
                WINNER1_C = WINNER1
            if WINNER2_C != WINNER2:
                STARTPLAYER = 2
                WINNER2_C = WINNER2
            while not quit:
                window.fill(BLACK)
                window.blit(background,(0,0))
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    # 玩家2操作逻辑
                    if GAME_WINDOW_OPT[4] == 1:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                if blank2_type == (10,150):
                                    blank2y_change = -10
                                if blank2_type == (10,100):
                                    blank2y_change = -15
                                if blank2_type == (10,200):
                                    blank2y_change = -6
                            if event.key == pygame.K_DOWN:
                                if blank2_type == (10,150):
                                    blank2y_change = 10
                                if blank2_type == (10,100):
                                    blank2y_change = 15
                                if blank2_type == (10,200):
                                    blank2y_change = 6
                            if event.key == pygame.K_RETURN:
                                    still = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                                blank2y_change = 0
                            if event.key == pygame.K_RETURN:
                                    still = False
                    # 玩家1操作逻辑
                    if GAME_WINDOW_OPT[3] == 1:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_w:
                                if blank1_type == (10,150):
                                    blank1y_change = -10
                                if blank1_type == (10,100):
                                    blank1y_change = -15
                                if blank1_type == (10,200):
                                    blank1y_change = -6
                            if event.key == pygame.K_s:
                                if blank1_type == (10,150):
                                    blank1y_change = 10
                                if blank1_type == (10,100):
                                    blank1y_change = 15
                                if blank1_type == (10,200):
                                    blank1y_change = 6
                                if event.key == pygame.K_RETURN:
                                        still = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_w or event.key == pygame.K_s:
                                blank1y_change = 0
                            if event.key == pygame.K_RETURN:
                                    still = False
                blank2_y += blank2y_change
                blank1_y += blank1y_change
                #球随板子动代码
                if still == True:
                        if STARTPLAYER == 1:
                            rect1 = rect1.move((blank1_x + 20)- rect1.left, (blank1_y + (blank1_type[1]- 10)/2)- rect1.top)
                        if STARTPLAYER == 2:
                             rect1 = rect1.move((blank2_x - 30)- rect1.left, (blank2_y + (blank2_type[1] - 10)/2)- rect1.top)
                #player1--AI系统
                if GAME_WINDOW_OPT[3] == 0:
                    miss1 = random.randint(1,20)
                    if speed[0] < 0:
                        if miss1 != 1:
                            if rect1.top > blank1_y+75 and blank1_type == (10,150):
                                c_speed = 10
                                blank1_y += 10
                            if rect1.top > blank1_y+100 and blank1_type == (10,200):
                                c_speed = 5
                                blank1_y += 5
                            if rect1.top > blank1_y+50 and blank1_type == (10,100):
                                c_speed = 15
                                blank1_y += 15
                            if rect1.bottom < blank1_y+100 and blank1_type == (10,200):
                                c_speed = 5
                                blank1_y += -5
                            if rect1.bottom < blank1_y+75 and blank1_type == (10,150):
                                c_speed = 10
                                blank1_y += -10
                            if rect1.bottom < blank1_y+50 and blank1_type == (10,100):
                                c_speed = 15
                                blank1_y += -15
                #player2--AI系统
                if GAME_WINDOW_OPT[4] == 0:
                    miss2 = random.randint(1,20)
                    if speed[0] > 0:
                        if miss2 != 1:
                            if rect1.top > blank2_y+75 and blank2_type == (10,150):
                                c_speed = 10
                                blank2_y += 10
                            if rect1.top > blank2_y+100 and blank2_type == (10,200):
                                c_speed = 5
                                blank2_y += 5
                            if rect1.top > blank2_y+50 and blank2_type == (10,100):
                                c_speed = 15
                                blank2_y += 15
                            if rect1.bottom < blank2_y+100 and blank2_type == (10,200):
                                c_speed = 5
                                blank2_y += -5
                            if rect1.bottom < blank2_y+75 and blank2_type == (10,150):
                                c_speed = 10
                                blank2_y += -10
                            if rect1.bottom < blank2_y+50 and blank2_type == (10,100):
                                c_speed = 15
                                blank2_y += -15
                # blanks边界处理逻辑
                if blank1_y <= 0:
                    blank1_y = 0
                    if STARTPLAYER == 1:
                        if still == True:
                            rect1 = rect1.move((blank1_x + 20)- rect1.left, (blank1_y + (blank1_type[1]- 10)/2)- rect1.top)
                if blank1_y >= 600 - blank1_type[1]:
                    blank1_y = 600 - blank1_type[1]
                    if STARTPLAYER == 1:
                        if still == True:
                            rect1 = rect1.move((blank1_x + 20)- rect1.left, (blank1_y + (blank1_type[1]- 10)/2)- rect1.top)
                if blank2_y <= 0:
                    blank2_y = 0
                    if STARTPLAYER == 2:
                        if still == True:
                            rect1 = rect1.move((blank2_x - 30)- rect1.left, (blank2_y + (blank2_type[1] - 10)/2)- rect1.top)
                if blank2_y >= 600 - blank2_type[1]:
                    blank2_y = 600 - blank2_type[1]
                    if STARTPLAYER == 2:
                        if still == True:
                            rect1 = rect1.move((blank2_x - 30)- rect1.left, (blank2_y + (blank2_type[1] - 10)/2)- rect1.top)
                # 球的运动处理逻辑
                if still == False:
                        rect1 = rect1.move(speed[0], speed[1])
                        if TIME == 0:
                            Time_c = 0
                            TIME += 1
                if rect1.top < 0 or rect1.bottom > height:
                    speed[1] = - speed[1]
                window.blit(swarm, rect1)
                # blank1&2碰撞处理逻辑
                if rect1.left <= 30:
                    if rect1.left >= 20:
                        if rect1.top >= blank1_y - 10:
                            if rect1.top <= (blank1_y + blank1_type[1]+ 10 ):
                                if speed[0] < 0:
                                    speed[0] = - speed[0]
                if rect1.left >= 10:
                            if rect1.left <= 40:
                                if rect1.bottom >= blank1_y - 5:
                                    if rect1.bottom <= blank1_y + 10:
                                        if speed[1] > 0:
                                            speed[1] = - speed[1]
                if rect1.left >= 10:
                            if rect1.left <= 40:
                                if rect1.top <= blank1_y + blank1_type[1] + 5:
                                    if rect1.top >= blank1_y + blank1_type[1] - 10:
                                        if speed[1] < 0:
                                            speed[1] = - speed[1]
                if rect1.right >= 970:
                    if rect1.right <= 980:
                        if rect1.top>= blank2_y - 10 :
                            if rect1.top <= (blank2_y + blank2_type[1] + 10) :
                                if speed[0] > 0:
                                    speed[0] = - speed[0]
                if rect1.right <= 990:
                    if rect1.right >= 960:
                        if rect1.bottom >= blank2_y - 5:
                            if rect1.bottom <= blank2_y + 10:
                                if speed[1] > 0:
                                    speed[1] = - speed[1]
                if rect1.right <= 990:
                    if rect1.right >= 960:
                        if rect1.top <= blank2_y + blank2_type[1] + 5:
                            if rect1.top >= blank2_y + blank2_type[1] - 10:
                                   if speed[1] < 0:
                                      speed[1] = - speed[1]
                #比分表
                text_display(window,str(scoreplayer2)+'     '+str(scoreplayer1),40,500,40,WHITE)
                #比分表逻辑&回合重置逻辑
                if rect1.left <= 0:
                    scoreplayer2 = scoreplayer_list[1] + 1
                    WINNER2 = scoreplayer_list.pop(1)
                    scoreplayer_list.insert(1,scoreplayer2)
                    break
                if rect1.right >= width:
                    scoreplayer1 = scoreplayer_list[0] + 1
                    WINNER1 = scoreplayer_list.pop(0)
                    scoreplayer_list.insert(0,scoreplayer1)
                    break
                #游戏结束重置逻辑
                if scoreplayer_list.count(rounds)!= 0:
                    RUNNING = False
                    GAME = 0
                    quit = True
                
                # 球随着时间的增加而加快
                Time_c += 1
                if Time_c % 600 == 0:
                    if speed[0]> 0:
                        if speed[0] < 9:
                            speed[0] = speed[0]+ 1
                    if speed[0] < 0:
                        if speed[0] > -9:
                            speed[0] = speed[0]-1
                    if speed[1]> 0:
                        if speed[1] < 9:
                            speed[1] += 1
                    if speed[1] < 0:
                        if speed[1] > -9:
                            speed[1] -= 1
                if blank1_type == (10,150):
                    blank1(BLUE,blank1_x,blank1_y,blank1_type[0],blank1_type[1])
                if blank1_type == (10,200):
                    blank1(BLUE,blank1_x,blank1_y,blank1_type[0],blank1_type[1])
                if blank1_type == (10,100):
                    blank1(BLUE,blank1_x,blank1_y,blank1_type[0],blank1_type[1])
                if blank2_type == (10,150):
                    blank2(RED,blank2_x,blank2_y,blank2_type[0],blank2_type[1])
                if blank2_type == (10,200):
                    blank2(RED,blank2_x,blank2_y,blank2_type[0],blank2_type[1])
                if blank2_type == (10,100):
                    blank2(RED,blank2_x,blank2_y,blank2_type[0],blank2_type[1])
                pygame.display.update()
#游戏结束画面
def game_ending ():
    game = True
    ending = pygame.display.set_mode((width,height))
    while game == True:
        ending.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text_display(ending,'Game Over',100,500,300,WHITE)
        pygame.draw.rect(ending,GREY,(450,420,100,50))
        pygame.draw.rect(ending,GREY,(450,500,100,50))
        if 450 < mouse[0] < 550 and 420 < mouse[1] < 500:
            pygame.draw.rect(ending,(150,150,150),(450,420,100,50))
            text_display(ending,'Again',35,499,447,WHITE)
            if click[0] == 1:
                restart = True
                return restart
        else:
            text_display(ending,'Again',30,499,447,WHITE)
        if 450 < mouse[0] < 550 and 500 < mouse[1] <550:
            pygame.draw.rect(ending,(150,150,150),(450,500,100,50))
            text_display(ending,'Exit',35,500,530,WHITE)
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            text_display(ending,'Exit',30,500,530,WHITE)

        
        clock.tick(60)
        pygame.display.update()


game_intro()
game_loop()
while True:
    x = game_ending()
    if x == True:
        game_loop()
