# coding=utf-8
from pygame import font, draw, init, display, transform, image, time, mouse, event, QUIT, MOUSEBUTTONUP
from settings import Setting
import sys


def text_objects(text, font, color):
    textsurf = font.render(text, True, color)
    return textsurf, textsurf.get_rect()


def text_display(window, color, text, size, coordinate, fonts):
    large_text = font.SysFont(fonts, size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = coordinate
    window.blit(text_surf, text_rect)


def blit_chess(team, chess, coor):
    img = Setting.img[str(team)+'_'+str(chess)]
    main_window.blit(img, [coor[0], coor[1], coor[2], coor[3]])
    if str(coors_plate[coor[2]][coor[3]])[1] == '0':
        coors_all[0].append(coor.copy())
    else:
        coors_all[1].append(coor.copy())


def show_all_selected():
    coor = [0, 32]
    for row in coors_plate:
        coor[0] = 37
        for col in row:
            if str(col)[-1] == '1':
                draw.circle(main_window, white, [coor[0]+30, coor[1]+30], 34,  3)
            coor[0] += 84
        coor[1] += 75


def draw_legal_moves(chess_name):
    for l_m in legal_move[coors_chess[chess_name]]:
        draw.circle(main_window, white, [40 + l_m[1] * 84, 37 + l_m[0] * 75], 34,  3)


def display_button(x, y, text, word_size, func):
    if x - word_size < Mouse[0] < x + word_size and y - word_size < Mouse[1] < y + word_size:
        text_display(main_window, black, text, word_size + 2, [x, y], 'simhei')
        if mouse_up:
            if func == 'hui_qi':
                hui_qi()
            elif func == 'new_game':
                new_game()
            elif func == 'save_game':
                save_game()
            elif func == 'load_game':
                load_game()
    else:
        text_display(main_window, black, text, word_size, [x, y], 'simhei')


def hui_qi():
    global who_go, hui_yi_bu
    if hui_yi_bu and start:
        try:
            return_c_coors_plate()
            who_go -= 1
            hui_yi_bu = False
        except:
            pass


def new_game():
    global coors_plate, start, load, who_go, over
    who_go = 0
    start, load, over = True, False, 0
    coors_plate.clear()
    for i in range(0, 10):
        coors_plate.append(temp[i].copy())


def save_game():
    with open('save.txt', 'w+') as save:
        for line in coors_plate:
            for index, coor in enumerate(line):
                if index != 8:
                    save.writelines(str(coor)+',')
                else:
                    save.writelines(str(coor))
            save.writelines('\n')
        save.writelines(str(who_go))


def load_game():
    global start, load, who_go, second_click, first_click, over
    start, load, second_click, first_click, over = False, True, False, True, 0
    coors_plate.clear()
    c_coors_plate.clear()
    for i in range(0, 10):
        coors_plate.append([])
    with open('save.txt', 'r+') as save:
        for index, line in enumerate(save.readlines()):
            if index != 10:
                for coor in line.split(','):
                    coors_plate[index].append(int(coor))
            else:
                who_go = int(line)


def clean_non_selected():
    for I, i in enumerate(coors_plate):
        for II, ii in enumerate(i):
            if str(ii)[-1] == '1':
                coors_plate[I][II] -= 1


def translation(coor):
    # window 800x800, chess 60x60, river_top 334, river_bot 394, b/w chess 84, startPt 37, 32
    x, y = coor[0], coor[1]
    coll = (x-37)//84
    if y <= 395:
        roww = (y-32)//75
    elif 395 < y < 410:
        return False
    else:
        roww = (y-32-15)//75
    return roww, coll


def click_chess(side):
    global first_click, second_click, first_click_coor, who_go, hui_yi_bu, start, chess
    if first_click:
        first_click_coor = [0, 0, 0]
        for coor in coors_all[side]:
            if coor[0] < Mouse[0] < coor[0] + 60 and coor[1] < Mouse[1] < coor[1] + 60:
                coors_plate[coor[2]][coor[3]] += 1
                first_click_coor[0], first_click_coor[1], first_click_coor[2] = \
                    coors_plate[coor[2]][coor[3]] - 1, coor[2], coor[3]
                chess = detect_legal_move(first_click_coor)
                current_chess.clear()
                current_chess.append(first_click_coor)
                first_click, second_click, start = False, True, True  # ??????????????????start = True???who_go????????????
                break
    elif second_click:
        clean_non_selected()
        for legal in legal_move[chess]:
            second_click_coor = translation(Mouse)
            if second_click_coor[0] == legal[0] and second_click_coor[1] == legal[1]:  # x1 == x2, y1 == y2
                update_c_coors_plate()
                if coors_plate[second_click_coor[0]][second_click_coor[1]] == 0 or \
                        str(coors_plate[second_click_coor[0]][second_click_coor[1]])[1] != str(side):
                    coors_plate[second_click_coor[0]][second_click_coor[1]] = first_click_coor[0]  # ??????????????????
                    coors_plate[first_click_coor[1]][first_click_coor[2]] = 0  # ??????????????????
                    who_go += 1
                    hui_yi_bu = True
                break
        first_click, second_click = True, False


def detect_legal_move(coor):
    chess_code = coors_plate[coor[1]][coor[2]]
    chess = coors_chess[str(chess_code)]
    legal_move[chess].clear()
    if chess == 'ju':
        left, right, up, down = True, False, True, False
        for horizon in range(0, 9):
            if left:
                if coors_plate[coor[1]][horizon] == 0:
                    legal_move[chess].append([coor[1], horizon])
                elif horizon == coor[2]:
                    left, right = False, True
                    continue
                elif coors_plate[coor[1]][horizon] != 0:
                    legal_move[chess].clear()
                    legal_move[chess].append([coor[1], horizon])
            elif right:
                if coors_plate[coor[1]][horizon] == 0:
                    legal_move[chess].append([coor[1], horizon])
                elif coors_plate[coor[1]][horizon] != 0:
                    legal_move[chess].append([coor[1], horizon])
                    break
        temp = len(legal_move[chess])
        for vertical in range(0, 10):
            if up:
                if coors_plate[vertical][coor[2]] == 0:
                    legal_move[chess].append([vertical, coor[2]])
                elif vertical == coor[1]:
                    up, down = False, True
                    continue
                elif coors_plate[vertical][coor[2]] != 0:
                    del legal_move[chess][temp:]
                    legal_move[chess].append([vertical, coor[2]])
            elif down:
                if coors_plate[vertical][coor[2]] == 0:
                    legal_move[chess].append([vertical, coor[2]])
                elif coors_plate[vertical][coor[2]] != 0:
                    legal_move[chess].append([vertical, coor[2]])
                    break
    elif chess == 'ma':
        for i, ma_tui in enumerate([[coor[1]-1, coor[2]], [coor[1]+1, coor[2]],
                       [coor[1], coor[2]-1], [coor[1], coor[2]+1]]):  # ????????????, ????????????
            try:
                ma_tui_s = {
                    0: [[ma_tui[0]-1, ma_tui[1]-1], [ma_tui[0]-1, ma_tui[1]+1]],  # ?????????
                    1: [[ma_tui[0]+1, ma_tui[1]-1], [ma_tui[0]+1, ma_tui[1]+1]],  # ?????????
                    2: [[ma_tui[0]+1, ma_tui[1]-1], [ma_tui[0]-1, ma_tui[1]-1]],  # ?????????
                    3: [[ma_tui[0]+1, ma_tui[1]+1], [ma_tui[0]-1, ma_tui[1]+1]]   # ?????????
                            }
                if coors_plate[ma_tui[0]][ma_tui[1]] == 0:
                    for ii in ma_tui_s[i]:
                        legal_move[chess].append(ii)
            except:
                pass
    elif chess == 'xiang':
        for i, xiang_tui in enumerate([[coor[1]-1, coor[2]-1], [coor[1]-1, coor[2]+1],
                                       [coor[1]+1, coor[2]-1], [coor[1]+1, coor[2]+1]]):
            try:
                xiang_tui_s = {
                    0: [xiang_tui[0]-1, xiang_tui[1]-1],
                    1: [xiang_tui[0]-1, xiang_tui[1]+1],
                    2: [xiang_tui[0]+1, xiang_tui[1]-1],
                    3: [xiang_tui[0]+1, xiang_tui[1]+1]
                }
                if coors_plate[xiang_tui[0]][xiang_tui[1]] == 0:
                    if who_go % 2 == 0 and xiang_tui_s[i][0] < 5:
                        legal_move[chess].append(xiang_tui_s[i])
                    elif who_go % 2 == 1 and xiang_tui_s[i][0] > 4:
                        legal_move[chess].append(xiang_tui_s[i])
            except:
                pass
    elif chess == 'shi' or chess == 'jiang' or chess == 'shuai':
        dics = {
            'shi': [[coor[1]-1, coor[2]-1], [coor[1]-1, coor[2]+1], [coor[1]+1, coor[2]+1], [coor[1]+1, coor[2]-1]],
            'jiang': [[coor[1]-1, coor[2]], [coor[1]+1, coor[2]], [coor[1], coor[2]-1], [coor[1], coor[2]+1]],
            'shuai': [[coor[1]-1, coor[2]], [coor[1]+1, coor[2]], [coor[1], coor[2]-1], [coor[1], coor[2]+1]]
        }
        if who_go % 2 == 1:
            for step in dics[chess]:
                if 2 < step[1] < 6 < step[0] < 10:
                    legal_move[chess].append(step)
        else:
            for step in dics[chess]:
                if -1 < step[0] < 3 and 2 < step[1] < 6:
                    legal_move[chess].append(step)
    elif chess == 'bing':
        if who_go % 2 == 0:
            if coor[1] < 5:
                legal_move[chess].append([coor[1]+1, coor[2]])
            else:
                for step in [[coor[1]+1, coor[2]], [coor[1], coor[2]-1], [coor[1], coor[2]+1]]:
                    legal_move[chess].append(step)
        else:
            if coor[1] > 4:
                legal_move[chess].append([coor[1]-1, coor[2]])
            else:
                for step in [[coor[1]-1, coor[2]], [coor[1], coor[2]-1], [coor[1], coor[2]+1]]:
                    legal_move[chess].append(step)
    elif chess == 'pao':
        all_horizon = []
        all_vertical = []
        for horizon in range(0, 9):
            all_horizon.append([coors_plate[coor[1]][horizon], [coor[1], horizon]])
        for vertical in range(0, 10):
            all_vertical.append([coors_plate[vertical][coor[2]], [vertical, coor[2]]])
        #  horizontal
        for times in range(0, 2):
            first = False
            all_horizon.reverse()
            index_h = all_horizon.index([chess_code, [coor[1], coor[2]]])
            for side in all_horizon[index_h+1:]:
                if side[0] == 0 and not first:
                    legal_move[chess].append(side[1])
                if first:
                    if side[0] != 0:
                        legal_move[chess].append(side[1])
                        first = False
                        break
                elif side[0] != 0:
                    first = True
                    continue
        # vertical
        for times in range(0, 2):
            first = False
            all_vertical.reverse()
            index_v = all_vertical.index([chess_code, [coor[1], coor[2]]])
            for side in all_vertical[index_v+1:]:
                if side[0] == 0 and not first:
                    legal_move[chess].append(side[1])
                if first:
                    if side[0] != 0:
                        legal_move[chess].append(side[1])
                        break
                elif side[0] != 0:
                    first = True
                    continue
    return chess


def game_over():
    x = 0
    jiang_shuai.clear()
    for i, row in enumerate(coors_plate):
        for ii, col in enumerate(row):
            if col == 5000 or col == 5100 or col == 5001 or col == 5101:
                x += 1
                jiang_shuai.append([i, ii])
    try:
        if jiang_shuai[0][1] == jiang_shuai[1][1] and x == 2:
            for i in range(jiang_shuai[0][0]+1, abs(jiang_shuai[1][0] - jiang_shuai[0][0])+1):
                if coors_plate[i][jiang_shuai[0][1]] != 0:
                    return x
                elif i == jiang_shuai[0][0]-1 or i == jiang_shuai[1][0]-1:
                    x = 1
                    return x
        else:
            return x
    except:
        return 1


def return_c_coors_plate():
    coors_plate.clear()
    for i in range(0, 10):
        coors_plate.append(c_coors_plate[i].copy())


def update_c_coors_plate():
    c_coors_plate.clear()
    for i in range(0, 10):
        c_coors_plate.append(coors_plate[i].copy())


init()

background = image.load('background.png')
background = transform.scale(background, (1000, 800))
window_width, window_height = 1000, 800
main_window = display.set_mode((window_width, window_height))
clock = time.Clock()
black = (0, 0, 0)
red = (255, 0, 0)
gray = (100, 100, 100)
white = (255, 255, 255)
who_go = 0  # even means red goes first, old means black goes first
chess = 0
start = False
load = False
first_click = True
second_click = False
mouse_up = False
hui_yi_bu = False

temp = Setting.coors_plate
coors_chess = Setting.coors_chess
legal_move = Setting.legal_move
coors_plate = []
c_coors_plate = []
current_chess = []
jiang_shuai = []
over = 0

while True:
    main_window.blit(background, (0, 0))
    Mouse = mouse.get_pos()
    click = mouse.get_pressed()
    coors = [0, 32, 0, 0, 0]
    coors_all = [[], []]
    non_chess_coors = []

    for i, row in enumerate(coors_plate):
        coors[0] = 37
        for ii, col in enumerate(row):
            coors[2], coors[3] = i, ii
            # red
            if col == 1010 or col == 1011 or col == 1020 or col == 1021:
                blit_chess('red', 'ju', coors)
            elif col == col == 2010 or col == 2011 or col == 2020 or col == 2021:
                blit_chess('red', 'ma', coors)
            elif col == 3010 or col == 3011 or col == 3020 or col == 3021:
                blit_chess('red', 'xiang', coors)
            elif col == col == 4010 or col == 4011 or col == 4020 or col == 4021:
                blit_chess('red', 'shi', coors)
            elif col == 5000 or col == 5001:
                blit_chess('red', 'shuai', coors)
            elif col == col == 6010 or col == 6011 or col == 6020 or col == 6021:
                blit_chess('red', 'pao', coors)
            elif col == 7010 or col == 7011 or col == 7020 or col == 7021 or col == 7030\
                    or col == 7031 or col == 7040 or col == 7041 or col == 7050 or col == 7051:
                blit_chess('red', 'bing', coors)
            # black
            elif col == 1110 or col == 1111 or col == 1120 or col == 1121:
                blit_chess('black', 'ju', coors)
            elif col == 2110 or col == 2111 or col == 2120 or col == 2121:
                blit_chess('black', 'ma', coors)
            elif col == 3110 or col == 3111 or col == 3120 or col == 3121:
                blit_chess('black', 'xiang', coors)
            elif col == 4110 or col == 4111 or col == 4120 or col == 4121:
                blit_chess('black', 'shi', coors)
            elif col == 5100 or col == 5101:
                blit_chess('black', 'jiang', coors)
            elif col == 6110 or col == 6111 or col == 6120 or col == 6121:
                blit_chess('black', 'pao', coors)
            elif col == 7110 or col == 7111 or col == 7120 or col == 7121 or col == 7130 \
                    or col == 7131 or col == 7140 or col == 7141 or col == 7150 or col == 7151:
                blit_chess('black', 'bing', coors)
            else:
                non_chess_coors.append(coors.copy())
            coors[0] += 84
        coors[1] += 75
    if current_chess:
        draw_legal_moves(str(current_chess[0][0]+1))
    show_all_selected()
    # ?????????
    display_button(900, 90, '?????????', 30, 'new_game')
    # ????????????
    display_button(900, 172, '??????', 30, 'save_game')
    # ????????????
    display_button(900, 633, '??????', 30, 'load_game')
    # ?????????
    display_button(900, 407, '?????????', 30, 'hui_qi')
    # ????????????
    if start or load:
        if who_go % 2 == 0:
            text_display(main_window, red, '?????????', 30, [900, 717], 'simhei')
        else:
            text_display(main_window, black, '?????????', 30, [900, 717], 'simhei')
        over = game_over()
        if over == 1:
            text_display(main_window, black, '????????????', 100, [window_width // 2, window_height // 2], 'simhei')

    mouse_up = False
    for Event in event.get():
        if Event.type == QUIT:
            sys.exit()
        if Event.type == MOUSEBUTTONUP:
            mouse_up = True
            if 385 > Mouse[1] or 425 < Mouse[1] and Mouse[0] < 800 and over != 1:
                if who_go % 2 == 0:
                    click_chess(0)  # eg. chess = [709, 707, 9, 8] - x, y, row, col
                elif who_go % 2 == 1:
                    click_chess(1)
    display.update()
    clock.tick()
