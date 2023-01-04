from PIL import ImageGrab
import cv2


# 截图窗口并只储存游戏窗口
def grab_image(left, top, right, bottom):
    rect = (left, top, right, bottom)
    img = ImageGrab.grab().crop(rect)
    return img


# 截图第y行第x列的blocks
def crop_blocks(img, y, x):
    x = 32*x
    y = 32*y
    img = img.crop((x, y, x+32, y+32))
    return img


# 将所有的blocks截取出来放在board_2d里面
def crop_image(img, blocks_x, blocks_y):
    # 空棋盘
    board_2d = [[0 for i in range(blocks_x)] for ii in range(blocks_y)]

    for i in range(blocks_y):
        for ii in range(blocks_x):
            board_2d[i][ii] = crop_blocks(img, i, ii)
    return board_2d
