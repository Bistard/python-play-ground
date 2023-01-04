from random import random
from math import sqrt
from multiprocessing import Process, Queue
import time


n = int(input())


def get_random_number(n, queue):
    in_circle = 0

    for i in range(n):

        random_x = random()
        random_y = random()

        if sqrt(random_x**2 + random_y**2) <= 1:
            in_circle += 1

    queue.put(in_circle)

queue = Queue()
processes = []

if __name__ == "__main__":
    start = time.time()
    for i in range(16):
        T = Process(target=get_random_number, args=(n, queue))
        processes.append(T)
        T.start()

    for p in processes:
        p.join()

    result = [queue.get() for j in processes]
    print(sum(result)/(n*16)*4)
    end = time.time()
    print(end-start)
