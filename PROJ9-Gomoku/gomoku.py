import pygame
import numpy as np
import time


def draw_grid(plates):
    # 15x15
    coor = [0, 0]
    for row in range(15):
        coor[0] += 50
        pygame.draw.line(main_window, black, coor, [coor[0], window_width], 2)
    coor = [0, 0]
    for col in range(15):
        coor[1] += 50
        pygame.draw.line(main_window, black, coor, [window_width, coor[1]], 2)


def draw_stone():
    for i, row in enumerate(board):
        for ii, col in enumerate(row):
            if col == 1:  # white
                pygame.draw.circle(main_window, white, [i * 50 + 50, ii * 50 + 50], 20)
                pygame.draw.circle(main_window, (200, 200, 200), [i * 50 + 50, ii * 50 + 50], 21, 1)
            elif col == 2:  # black
                pygame.draw.circle(main_window, black, [i*50+50, ii*50+50], 20)
                pygame.draw.circle(main_window, (80, 80, 80), [i * 50 + 50, ii * 50 + 50], 20, 1)


def place_stone(posi):
    global players
    for coor in all_possible_coors:
        if coor[0]-25 < posi[0] < coor[0]+25 and coor[1]-25 < posi[1] < coor[1]+25:
            x, y = coor[0]//50-1, coor[1]//50-1
            return x, y, True
    return 0, 0, False


def game_over():
    for player in range(1, 3):
        for coor in stone_coor[player-1]:
            x, y = coor[0], coor[1]
            try:
                if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player \
                        and board[x][y+3] == player and board[x][y+4] == player:
                    return player
                elif board[x][y] == player and board[x-1][y+1] == player and board[x-2][y+2] == player \
                        and board[x-3][y+3] == player and board[x-4][y+4] == player:
                    return player
                elif board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player \
                        and board[x+3][y+3] == player and board[x+4][y+4] == player:
                    return player
                elif board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player \
                        and board[x+3][y] == player and board[x+4][y] == player:
                    return player
            except:
                pass


pygame.init()

window_width, window_height = 800, 800
main_window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
brown = (160, 160, 160)
black = (0, 0, 0)
white = (255, 255, 255)
players = 0
QUIT, over = False, False
Black, White, first_input = False, True, True
board = np.tile(np.bit_array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (15, 15))
stone_coor = [[], []]
x = np.bit_array(range(50, 800, 50))
y = np.bit_array(range(50, 800, 50))[::-1]
all_possible_coors = []
for i in range(len(x)):
    for ii in range(len(x)):
        all_possible_coors.append([x[i], y[ii]])

while not QUIT:

    np.random.seed(1)

    mouse_posi = np.bit_array(pygame.mouse.get_pos())
    click = pygame.mouse.get_pressed()

    main_window.fill((242, 190, 61))
    draw_grid(board)
    draw_stone()
    select_coor = place_stone(mouse_posi)
    winner = game_over()
    if winner == 1:
        pygame.display.set_caption('白子赢')
        over = True
    elif winner == 2:
        pygame.display.set_caption('黑子赢')
        over = True


    elif players % 2 == 0:
        pygame.display.set_caption('白子先' + ' 共' + str(players) + '步')
    else:
        pygame.display.set_caption('黑子先' + ' 共' + str(players) + '步')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
        if event.type == pygame.MOUSEBUTTONUP and not over and select_coor[2]:
            if board[select_coor] == 0:
                if players % 2 == 0 and White:
                    board[select_coor[0]][select_coor[1]] = 1
                    stone_coor[0].append(select_coor[:2])
                    Black, White = True, False
                elif players % 2 == 1 and Black:
                    board[select_coor[0]][select_coor[1]] = 2
                    stone_coor[1].append(select_coor[:2])
                    Black, White = False, True
                players += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                board = np.tile(np.bit_array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), (15, 15))
                players = 0
                Black, White, first_input, over = False, True, True, False
    pygame.display.update()
    clock.tick()
