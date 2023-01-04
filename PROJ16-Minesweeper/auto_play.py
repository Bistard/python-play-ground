from ctypes import windll
import win32gui
import ImageProgress as IP
import BlockAnalysis as BA
import Simple_Algorithm as SA
import Tank_Algorithm as TA
import time
from tkinter import _flatten

# 调整DPI (看情况删除)
user32 = windll.user32
user32.SetProcessDPIAware()

# 窗口获取
class_name = "TMain"
title_name = "Minesweeper Arbiter"  # 如果找不到窗口试着在string最后打一个空格

window_position = win32gui.FindWindow(class_name, title_name)  # 如果没有找到window会返回0
if window_position:
    left, top, right, bottom = win32gui.GetWindowRect(window_position)
    # 参数
    left += 30
    top += 202
    right -= 30
    bottom -= 86
else:  # 主动抛出异常
    raise Exception("Window not found.")

# 参数
block_side = 32
# 计算共几列几行
blocks_x = (right - left) // block_side
blocks_y = (bottom - top) // block_side

# 默认新游戏
restart = True

while True:
    time.sleep(0.2)
    # 将棋盘分割
    whole_board = IP.grab_image(left, top, right, bottom)
    board_2d = IP.crop_image(whole_board, blocks_x, blocks_y)

    all_blocks = []  # 储存所有数字的坐标
    all_flags = []  # 储存所有旗子的坐标

    #
    # 每一次restart之后, 进行一次纯随机点
    # 分析每一个方块(img)然后将它转换为数字(int)
    result = BA.analysis_all_blocks(board_2d, blocks_x, blocks_y, left, top, all_flags, all_blocks)

    if result:
        restart = False
        SA.brand_new_start(block_side, blocks_x, blocks_y, left, top)
        continue

    # 基础算法-标棋子
    for block in all_blocks:
        flags = SA.mark_each_block(board_2d, block, all_flags, block_side, left, top, blocks_x, blocks_y)
        if flags is not None:
            all_flags += flags

    dead = True
    # 基础算法-点雷块
    for block in all_blocks:
        result = SA.click_each_block(board_2d, block, block_side, left, top, blocks_x, blocks_y)
        if result:
            dead = False

    # DFS深度优先搜索-寻找边缘
    all_board_tiles = []  # 所有合法的board_tiles的坐标都在这里, 用来防止重复计算.
    all_board_tiles_unclick = []  # 储存每个board_tiles所包括未点击雷块的所有坐标.
    if dead:
        already_done = []  # 单纯的用来好计算 (此功能可以简化, 但是我暂时不想写)
        for block in all_blocks:  # 检查所有的数字方块.
            if block not in already_done:  # 防止重复
                board_tiles = []  # 储存边缘的坐标
                TA.enumerate_board_tiles(board_tiles, board_2d, block[0], block[1], blocks_x, blocks_y)
                already_done += set(board_tiles)  # 更新所有合法的board_titles
                if board_tiles:
                    all_board_tiles.append(list(set(board_tiles)))

        #  获得每个board_tile所包括的未点击雷块的坐标
        for board_tiles in all_board_tiles:
            unclick_each_board_tiles = []
            for board_tile in board_tiles:
                row, col = board_tile[0], board_tile[1]
                coor_unclick = BA.find_surround_type(board_2d, row, col, blocks_x, blocks_y, (0,))[1]
                for coor in coor_unclick:
                    unclick_each_board_tiles.append(coor)
            all_board_tiles_unclick.append(list(set(unclick_each_board_tiles)))

        # 此算法会忽略掉一种情况, 导致1整个board_tile被判定为2个board_tiles.
        # 作为解决办法, 检测每个board_tile包括所有未点击雷块之间的坐标是否有交集, 如果有(代表互相影响彼此), 就整合在一起.
        all_board_tiles_unclick = TA.combine_board_tiles(all_board_tiles_unclick)


    # DFS-求出概率
    for board_tiles_unclick in all_board_tiles_unclick:
        all_possibles_each_board_tile = []
        possible_each_board_tile = []
        marked_flag, marked_zero = [], []
        TA.enumerate_all_possibles(marked_flag, marked_zero, all_possibles_each_board_tile, possible_each_board_tile, 0, board_2d, board_tiles_unclick, blocks_x, blocks_y)
        print(len(all_possibles_each_board_tile), len(board_tiles_unclick))


        possibilities = [0 for i in range(len(board_tiles_unclick))]
        for i, possibility in enumerate(all_possibles_each_board_tile):
            for ii, each_tile_possibility in enumerate(possibility):
                possibilities[ii] += each_tile_possibility
        print(possibilities)
        minimum_possibility = min(possibilities)

        for i, p in enumerate(possibilities):
            if p == minimum_possibility:
                coor = board_tiles_unclick[i]
                SA.single_click(coor, 1, block_side, left, top)
                dead = False


    if dead:  # Tank_Algorithm也解决不了的时候. 纯随机点击.
        time.sleep(0.1)
        #SA.guess(board_2d, block_side, blocks_x, blocks_y, left, top)
        pass
