import numpy as np
import pandas as pd
import csv

model_name = 'model.csv'
alpha = 0.9


def write_csv(file, lines, data):
    with open(file, 'a', newline='') as model:
        model = csv.writer(model)
        for i in range(lines):
            model.writerow(data)


def cal_reward(state, board):
    for player in range(1, 3):
        for stone in state[player-1]:
            x, y = stone[0], stone[1]

    return


def first_input(board, side, state):  # 黑棋先
    if side % 2 == 1:
        while True:
            rand_x, rand_y = np.random.randint(15), np.random.randint(15)
            if board[rand_x][rand_y] == 0:
                break
        board[rand_x][rand_y] = 2
        s = state[0]+state[1]
        r = cal_reward(state, board)
        data = [s, [rand_x, rand_y], '']
        write_csv(model_name, 1, data)
        return rand_x, rand_y


def self_play(board, side, state):
    if side % 2 == 1:
        data = pd.read_csv(model_name)
        cal_reward(state, board)

        #print(data.head(100))
