from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random

# 鼠标/键盘信号
m = PyMouse()
k = PyKeyboard()


# 用来点击
def single_click(coordinate, right_left, block_side, x, y):
    row = coordinate[0]
    col = coordinate[1]
    actual_x = x + block_side * col + 16
    actual_y = y + block_side * row + 16
    m.click(actual_x, actual_y, right_left)


# 纯随机开局 (只适用于"开局")
def brand_new_start(block_side, block_x, block_y, x, y):
    rand_row = random.randint(0, block_y-1)
    rand_col = random.randint(0, block_x-1)
    actual_x = x + block_side * rand_col + 16
    actual_y = y + block_side * rand_row + 16
    m.click(actual_x, actual_y, 1)


# 随机点击雷块 (只适用于"死局")
# 1.0版本:只要click_each_block返回True(一次有效左击都没有), 则纯随机选择block.
# 2.0版本:只选择周围有数字的block进行点击. 实际测试下来效果更佳.
def guess(board, block_side, block_x, block_y, x, y):
    available = False
    while True:
        col = random.randint(0, block_x-1)
        row = random.randint(0, block_y-1)
        surrounding = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                       (row, col - 1), (row, col + 1),
                       (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        # 看看该随机方块周围有没有数字
        if not board[row][col]:
            for sr in surrounding:
                # 考虑到边缘旗子的特殊性, 如果坐标在棋盘外面则略过
                if sr[0] != -1 and sr[0] != block_y and sr[1] != -1 and sr[1] != block_x:
                    if board[sr[0]][sr[1]] not in (-2, -1, 0, 9):
                        available = True
            if available:
                break
    actual_x = x + block_side * col + 16
    actual_y = y + block_side * row + 16
    m.click(actual_x, actual_y, 1)


# 点击笑脸重开
def restart(x, y):
    m.click(x+40, y-58, 1)


# 标记雷块
def mark_each_block(board, block, all_flags, block_side, x, y, block_x, block_y):
    row = block[0]
    col = block[1]
    number = board[row][col]
    # 周围八个相对坐标
    surrounding = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                   (row, col - 1), (row, col + 1),
                   (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    # 储存这个方块周围的未点击方块数量
    un_clicks = []
    for sr in surrounding:
        # 考虑到边缘旗子的特殊性, 如果坐标在棋盘外面则略过
        if sr[0] != -1 and sr[0] != block_y and sr[1] != -1 and sr[1] != block_x:
            if not board[sr[0]][sr[1]] or board[sr[0]][sr[1]] == -2:
                un_clicks.append(sr)

    # 如果周围未点击数量和自身数字相同
    if len(un_clicks) == number:
        for flag in un_clicks:
            # 算出实际的点击坐标
            actual_x = x + block_side * flag[1] + 16
            actual_y = y + block_side * flag[0] + 16
            if flag not in all_flags:  # 防止二次以上的点击
                m.click(actual_x, actual_y, 2)
                board[flag[0]][flag[1]] = -2
        return un_clicks


def click_each_block(board, block, block_side, x, y, block_x, block_y):
    row = block[0]
    col = block[1]
    number = board[row][col]
    # 周围八个相对坐标
    surrounding = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                   (row, col - 1), (row, col + 1),
                   (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    # 储存这个方块周围旗子的数量
    flags = []
    # 储存这个方块还未点击方块的数量
    un_click = []
    for sr in surrounding:
        # 考虑到边缘旗子的特殊性, 如果坐标在棋盘外面则略过
        if sr[0] != -1 and sr[0] != block_y and sr[1] != -1 and sr[1] != block_x:
            if board[sr[0]][sr[1]] == -2:
                flags.append(sr)
            elif not board[sr[0]][sr[1]]:
                un_click.append(sr)

    if len(flags) == number and len(un_click):
        actual_x = x + block_side * col + 16
        actual_y = y + block_side * row + 16
        m.click(actual_x, actual_y, 3)
        return True  # 代表点击过
    return False  # 代表没有点击过
