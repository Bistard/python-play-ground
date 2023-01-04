import Simple_Algorithm as SA
"""
1~8: 代表1~8数字
9: 地雷
0: 还未点击
-1: 点击之后是空白
-2: 棋子
"""


def analysis_all_blocks(img, block_x, block_y, left, top, all_flags, all_blocks):
    for i in range(block_y):
        for ii in range(block_x):
            block = analysis_each_block(img, i, ii)
            if block == 'mine':
                #SA.restart(left, top)
                return True
            elif block == 'flag':
                all_flags.append((i, ii))
            elif block is not None:
                all_blocks.append(block)
    return False


# 分析每一个方块
def analysis_each_block(img, y, x):
    # 检测炸弹
    if img[y][x].getpixel((14, 14)) == (255, 255, 255):
        img[y][x] = 9
        return 'mine'
    # 检测未点击的空白 和 棋子
    elif img[y][x].getpixel((0, 0)) == (255, 255, 255):
        if img[y][x].getpixel((16, 16)) == (0, 0, 0):
            img[y][x] = -2
            return 'flag'
        else:
            img[y][x] = 0
    # 检测点击后的空白
    elif img[y][x].getpixel((4, 4)) == (192, 192, 192) and img[y][x].getpixel((16, 16)) == (192, 192, 192):
            img[y][x] = -1
    # 检测1
    elif img[y][x].getpixel((16, 16)) == (0, 0, 255):
        img[y][x] = 1
    # 检测2
    elif img[y][x].getpixel((16, 16)) == (0, 128, 0):
        img[y][x] = 2
    # 检测3
    elif img[y][x].getpixel((16, 16)) == (255, 0, 0):
        img[y][x] = 3
    # 检测4
    elif img[y][x].getpixel((16, 16)) == (0, 0, 128):
        img[y][x] = 4
    # 检测5
    elif img[y][x].getpixel((16, 16)) == (128, 0, 0):
        img[y][x] = 5
    # 检测6
    elif img[y][x].getpixel((16, 16)) == (0, 128, 128):
        img[y][x] = 6
    # 检测7
    elif img[y][x].getpixel((18, 16)) == (0, 0, 0):
        img[y][x] = 7
    # 检测8
    elif img[y][x].getpixel((16, 16)) == (128, 128, 128):
        img[y][x] = 8
    else:
        raise Exception('Couldn\'t screenshot the window.')
    # 只会返回数字的坐标(并且不包括边缘的数字), 否则返回None
    return (y, x) if img[y][x] in (1, 2, 3, 4, 5, 6, 7, 8) else None


# 用来记录一个特定方块周围八个之内所需要求种类雷块的数量和坐标
def find_surround_type(board, row, col, block_x, block_y, type, type2=(None,), type3=(None,)):
    # 周围8个的相对坐标
    count_type = 0
    coors_type = []
    count_type2 = 0
    coors_type2 = []
    count_type3 = 0
    coors_type3 = []

    surrounding = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                   (row, col + 1), (row + 1, col + 1), (row + 1, col),
                   (row + 1, col - 1), (row, col - 1)]
    for sr in surrounding:
        if sr[0] != -1 and sr[0] != block_y and sr[1] != -1 and sr[1] != block_x:  # 考虑到棋盘的边缘性.
            if board[sr[0]][sr[1]] in type:
                count_type += 1
                coors_type.append(sr)
            if board[sr[0]][sr[1]] in type2:
                count_type2 += 1
                coors_type2.append(sr)
            if board[sr[0]][sr[1]] in type3:
                count_type3 += 1
                coors_type3.append(sr)

    if type2 == (None,):
        return count_type, coors_type
    elif type3 == (None,):
        return count_type, coors_type, count_type2, coors_type2
    else:
        return (count_type, coors_type), (count_type2, coors_type2), (count_type3, coors_type3)
