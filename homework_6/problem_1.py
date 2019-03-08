import numpy as np
import matplotlib.pyplot as plt


def linear_spline(x, y):
    plt.plot(x, y)
    plt.show()


linear_spline([i for i in range(10)], [2, 1, 4, 2, 6, 7, 6, 1, 7, 3])
