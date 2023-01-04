import pygame
import random
from tkinter import _flatten


def bubble_sort():
    global index, sort
    if len(List) == 1:
        sort = 0
        stack.insert(0, List.pop(index))
        return
    if List[index] > List[index+1]:
        List[index], List[index+1] = List[index+1], List[index]
    index += 1
    if index == len(List)-1:
        stack.insert(0, List.pop(index))
        index = 0

    x, y = 0, 800
    for i, num in enumerate(List + stack):
        if num in stack:
            colors[i] = GREEN
        elif i == index:
            colors[i] = RED
        else:
            colors[i] = GREY
        pygame.draw.rect(window, colors[i], [x, 800 - num * height_data, width_data, num * 10])
        x += gap_data


def selection_sort():
    global index, index2, sort
    if index == len(List)-1:
        sort = 0
        colors[index] = GREEN
        stack.clear()
        return
    if List[index] > List[index2]:
        List[index], List[index2] = List[index2], List[index]
    if index2 == len(List)-1:
        stack.append(List[index])
        index += 1
        index2 = index
    index2 += 1

    x, y = 0, 800
    for i, num in enumerate(List):
        if num in stack:
            colors[i] = GREEN
        elif i == index2:
            colors[i] = RED
        else:
            colors[i] = GREY
        pygame.draw.rect(window, colors[i], [x, 800 - num * height_data, width_data, num * 10])
        x += gap_data


def insertion_sort():
    global index, sort
    if not List:
        sort = 0
        return
    if not stack:
        stack.insert(0, List.pop(0))
    elif List[0] < stack[index]:
        stack.insert(index, List.pop(0))
        index = 0
    elif index == len(stack)-1:
        stack.append(List.pop(0))
        index = 0
    elif List[0] > stack[index]:
        index += 1

    x, y = 0, 800
    for i, num in enumerate(List + stack):
        if num in stack:
            colors[i] = GREEN
        elif i == index:
            colors[i] = RED
        else:
            colors[i] = GREY
        pygame.draw.rect(window, colors[i], [x, 800 - num * height_data, width_data, num * 10])
        x += gap_data


def merge_sort():
    global index, index2, sort, List, colors
    if len(List) == 1:
        List = list(_flatten(List))
        List.sort()
        sort = 0
        colors = [GREEN for i in range(1, num_data)]
        return
    if isinstance(List[-1], int):
        index2 = 0
        while isinstance(List[-1], int):
            List.insert(0, [List.pop(-2), List.pop(-1)])
    if index == len(List)-1:
        index, index2 = 0, 0
        for i in range(len(List)//2):
            List.insert(0, sorted(List.pop(-2))+sorted(List.pop(-1)))
    if index2 == len(List[index])-1:
        index2 = 0
        index += 1
    if List[index][index2] > List[index][index2+1]:
        List[index][index2], List[index][index2+1] = List[index][index2+1], List[index][index2]
        index2 += 1
    else:
        index2 += 1

    x, y = 0, 800
    temp = list(_flatten(List))
    for i, num in enumerate(temp):
        if num == i:
            colors[i] = GREEN
        else:
            colors[i] = GREY
        pygame.draw.rect(window, colors[i], [x, 800 - num * height_data, width_data, num * 10])
        x += gap_data

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (180, 180, 180)
GREEN = (34, 177, 76)
BLUE = (34, 76, 177)
window_width, window_height = 1200, 800
num_data = 103
gap_data = window_width//(num_data-1)
width_data = gap_data-2
height_data = 6

clock = pygame.time.Clock()
window = pygame.display.set_mode((window_width, window_height))

List = [i for i in range(1, num_data)]  # 1~50随机顺序的数字
colors = [GREY for i in range(1, num_data)]
random.shuffle(List)
stack, stack2 = [], []
index, index2, sort, count = 0, 1, 0, 0

while True:
    window.fill(BLACK)
    if not sort:
        x, y = 0, 800
        for i, num in enumerate(List + stack):
            pygame.draw.rect(window, colors[i], [x, 800 - num * height_data, width_data, num * 10])
            x += gap_data
    elif sort:
        if sort == 1:
            bubble_sort()
        elif sort == 2:
            selection_sort()
        elif sort == 3:
            insertion_sort()
        elif sort == 4:
            merge_sort()
        elif sort == 5:
            pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if not sort and event.key == pygame.K_r:
                List = [i for i in range(1, num_data)]  # 1~50随机顺序的数字
                colors = [GREY for i in range(1, num_data)]  # 1~50随机顺序的数字
                random.shuffle(List)
                stack, index, index2 = [], 0, 1
            if event.key == pygame.K_1:  # bubble sort
                sort = 1
            elif event.key == pygame.K_2:  # selection sort
                sort = 2
            elif event.key == pygame.K_3:  # insertion sort
                sort = 3
            elif event.key == pygame.K_4:
                sort = 4
            elif event.key == pygame.K_5:
                sort = 5
            elif event.key == pygame.K_6:
                sort = 6
            elif event.key == pygame.K_7:
                sort = 7
            elif event.key == pygame.K_8:
                sort = 8

    pygame.display.update()
    clock.tick()
