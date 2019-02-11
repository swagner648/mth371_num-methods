import matplotlib.pyplot as plt
from eulerlib.prime_numbers import *


def prime_spiral_grid(n):
    grid = [[0 for i in range(n)] for j in range(n)]
    x = n // 2 - 1
    y = n // 2 - 1
    length = 1
    grid[y][x] = 0
    count = 2
    while True:
        interval = (-1) ** (abs(length) + 1)
        for i in range(x + interval, x + length + interval, interval):
            if i == -1:
                return grid
            grid[y][i] = 1 if is_prime(count) else 0
            count += 1
        x += length
        for i in range(y + interval, y + length + interval, interval):
            grid[i][x] = 1 if is_prime(count) else 0
            count += 1
        y += length
        length = (-1)**(abs(length) + 2) * (abs(length) + 1)


grid = prime_spiral_grid(400)
plt.figure(figsize=(100, 100))
plt.title('400 x 400')
plt.imshow(grid)
plt.show()
