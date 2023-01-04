"""
广度优先算法BFS
寻找board_tiles
"""
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random
import BlockAnalysis as BA


# DFS-深度优先搜索
# 来搜索所有雷块所包括的边界
def enumerate_board_tiles(board_tile, board, row, col, block_x, block_y):

    sub_degree = []  # 储存周围8个数字雷块的坐标
    any_number = False  # 判断周围8个是否有任何数字雷块
    any_unclicked = False  # 判断周围8个是否有任何可点击雷块 -> 从而判断目前方块是否是合法board_tile

    # 周围8个的相对坐标
    surrounding = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]

    for sr in surrounding:
        if sr[0] != -1 and sr[0] != block_y and sr[1] != -1 and sr[1] != block_x:  # 考虑到棋盘的边缘性.
            number = board[sr[0]][sr[1]]

            # 将可能称为board_tile的坐标储存在sub_degree里面.
            if number in (1, 2, 3, 4, 5, 6, 7, 8) and sr not in board_tile:
                sub_degree.append(sr)
                any_number = True

            # 判断目前的雷块是否属于合法board_tile
            elif not number:
                any_unclicked = True

    if any_unclicked:

        board_tile.append((row, col))

        if any_number:
            for block in sub_degree:
                enumerate_board_tiles(board_tile, board, block[0], block[1], block_x, block_y)


# 此算法会忽略掉一种情况, 导致1整个board_tile被判定为2个board_tiles.
# 作为解决办法, 检测每个board_tile包括所有未点击雷块之间的坐标是否有交集, 如果有(代表互相影响彼此), 就整合在一起.
def combine_board_tiles(all_board_tiles_unclick):
    new_all_board_tile_unclick = []
    for i in range(len(all_board_tiles_unclick)-1):
        board_tiles_unclick = all_board_tiles_unclick[i]
        for ii in range(i+1, len(all_board_tiles_unclick)):
            compare = all_board_tiles_unclick[ii]
            if set(all_board_tiles_unclick[i]).intersection(set(all_board_tiles_unclick[ii])):
                new_all_board_tile_unclick.append(list(set(all_board_tiles_unclick[i] + all_board_tiles_unclick[ii])))
                all_board_tiles_unclick.remove(board_tiles_unclick)
                all_board_tiles_unclick.remove(compare)
                return combine_board_tiles(new_all_board_tile_unclick + all_board_tiles_unclick)
    return all_board_tiles_unclick


# DFS-深度优先搜索
# 搜索board_tile雷区的所有可能的排列组合
def enumerate_all_possibles(marked_flag, marked_zero, ap, p, start, board, board_tile_unclick, block_x, block_y):

    cr = board_tile_unclick[start]
    status = None  # 这行没必要, 写上来只是好看

    coors_numbers = BA.find_surround_type(board, cr[0], cr[1], block_x, block_y, (1, 2, 3, 4, 5, 6, 7, 8))[1]

    for number in coors_numbers:
        current_number = board[number[0]][number[1]]

        type1, type2, type3 = (-2,), (0,), (-2, 0)
        types = BA.find_surround_type(board, number[0], number[1], block_x, block_y, type1, type2, type3)
        count_flag, coors_flag = types[0]
        count_zero, coors_zero = types[1]
        count_every, coors_every = types[2]

        for zero in marked_zero:  #
            if zero in coors_zero:
                count_zero -= 1
        for flag in marked_flag:
            if flag in coors_every:
                count_flag += 1

        # 0代表该方块没有炸弹, 1则代表有.
        if count_flag == current_number:  # 该方块只能是0.
            status = '0'
            break
        elif count_zero == 1:  # 该方块只能是1.
            status = '1'
            break
        else:  # 该方块可以是0或者1.
            status = 'either'

    if status == 'either':
        for i in [0, 1]:
            if start != len(board_tile_unclick) - 1: # 因为遍历所有unclick的坐标的时候不是按一个接着一个来的, 所以会有可能出现bug
                marked_zero.append(cr) if not i else marked_flag.append(cr)
                p.append(i)
                enumerate_all_possibles(marked_flag, marked_zero, ap, p, start+1, board, board_tile_unclick, block_x, block_y)
                marked_zero.remove(cr) if not i else marked_flag.remove(cr)
                p.pop(-1)

    elif status == '1':
        p.append(1)
        if start != len(board_tile_unclick) - 1:
            marked_flag.append(cr)
            enumerate_all_possibles(marked_flag, marked_zero, ap, p, start+1, board, board_tile_unclick, block_x, block_y)
            marked_flag.remove(cr)
        else:
            ap.append(p.copy())
        p.pop(-1)

    elif status == '0':
        p.append(0)
        if start != len(board_tile_unclick) - 1:
            marked_zero.append(cr)
            enumerate_all_possibles(marked_flag, marked_zero, ap, p, start+1, board, board_tile_unclick, block_x, block_y)
            marked_zero.remove(cr)
        else:
            ap.append(p.copy())
        p.pop(-1)
