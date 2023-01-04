import pygame
import sys
import time

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window_width, window_height = 1200, 800
clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height))

cell_size = 5
board = [[0 for ii in range(window_width//cell_size)] for i in range(window_height//cell_size)]


def count_cells():
    check = []
    for i, row in enumerate(board):
        copy_row = row.copy()
        while 1 in copy_row:
            ii = copy_row.index(1)

            if not i:
                for cell in ((i+1, ii-1), (i+1, ii), (i+1, ii+1)):
                    try:
                        if cell not in check:
                            state = survive(cell)
                            check.append(cell)
                            check.append(state)
                    except IndexError:
                        pass
            elif i == len(board)-1:
                for cell in ((i-1, ii-1), (i-1, ii), (i-1, ii+1)):
                    try:
                        if cell not in check:
                            state = survive(cell)
                            check.append(cell)
                            check.append(state)
                    except IndexError:
                        pass
            else:
                for cell in ((i+1, ii-1), (i+1, ii), (i+1, ii+1), (i-1, ii-1), (i-1, ii), (i-1, ii+1)):
                    try:
                        if cell not in check:
                            state = survive(cell)
                            check.append(cell)
                            check.append(state)
                    except IndexError:
                        pass

            for cell in ((i, ii-1), (i, ii), (i, ii+1)):
                try:
                    if cell not in check:
                        state = survive(cell)
                        check.append(cell)
                        check.append(state)
                except IndexError:
                    pass

            copy_row.pop(ii)
            copy_row.insert(ii, 0)
    return check


def next_round(check):
    for cell in range(0, len(check), 2):
        board[check[cell][0]][check[cell][1]] = check[cell+1]


def survive(coors):
    i, ii = coors
    count = 0
    if not i:
        for x, y in ((i + 1, ii - 1), (i + 1, ii), (i + 1, ii + 1)):
            try:
                if board[x][y]:
                    count += 1
            except IndexError:
                pass
    elif i == len(board) - 1:
        for x, y in ((i - 1, ii - 1), (i - 1, ii), (i - 1, ii + 1)):
            try:
                if board[x][y]:
                    count += 1
            except IndexError:
                pass
    else:
        for x, y in ((i + 1, ii - 1), (i + 1, ii), (i + 1, ii + 1), (i - 1, ii - 1), (i - 1, ii), (i - 1, ii + 1)):
            try:
                if board[x][y]:
                    count += 1
            except IndexError:
                pass

    for x, y in ((i, ii - 1), (i, ii + 1)):
        try:
            if board[x][y]:
                count += 1
        except IndexError:
            pass
    if board[i][ii]:
        if count < 2 or count > 3:
            return 0
        else:
            return 1

    elif not board[i][ii]:
        if count == 3:
            return 1
        else:
            return 0


def mainloop():

    global board
    start = False
    caption = 'Pause'
    FPS = 60

    while True:
        m = pygame.mouse.get_pos()
        pygame.display.set_caption(caption)
        window.fill(BLACK)

        if start:
            start = time.perf_counter()
            x = count_cells()
            next_round(x)
            end = time.perf_counter()
            print(end-start)

        x, y = 0, 0
        for row in board:
            x = 0
            for col in row:
                if col:
                    pygame.draw.rect(window, WHITE, (x, y, cell_size, cell_size))
                x += cell_size
            y += cell_size

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_F12:
                    FPS += 1
                if event.key == pygame.K_F11 and FPS >= 0:
                    FPS -= 1
                if event.key == pygame.K_RETURN:
                    if not start:
                        start = True
                        caption = 'Running'
                    elif start:
                        start = False
                        caption = 'Pause'

                elif event.key == pygame.K_ESCAPE:
                    start = False
                    caption = 'Pause'
                    board = board = [[0 for ii in range(window_width//cell_size)] for i in range(window_height//cell_size)]

            elif event.type == pygame.MOUSEBUTTONUP:
                if not start:
                    x, y = m[0]//cell_size, m[1]//cell_size
                    if not board[y][x]:
                        board[y][x] = 1
                    else:
                        board[y][x] = 0

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    while True:
        mainloop()
