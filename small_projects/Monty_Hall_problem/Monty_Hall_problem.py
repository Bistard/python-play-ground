import random
times = 1000000

for change in [True, False]:  # True means to switch the door; False means not to switch the door.
    win, lost = 0, 0
    for i in range(times):
        doors = [0, -1, 1]  # 0 represents monty hall, -1 represents empty, 1 represents the car.
        pick = random.choice(doors)
        if not change:  # in this case, change = False.
            if pick == 1:
                win += 1
            else:
                lost += 1
        else:  # in this case, change = True.
            if pick == 1:
                lost += 1
            else:
                win += 1
    if change:
        print('if you change to the other door:', str(win / (win + lost) * 100) + '%')
    else:
        print('if you keep your choice:', str(win / (win + lost) * 100) + '%')

