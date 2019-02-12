import matplotlib.pyplot as plt
import numpy as np


x = list(np.arange(0.998, 1, 0.0001))
y = [(i-1)**7 for i in x]
plt.plot(x, y)
plt.title("Method 1")
plt.show()


def f(n):
    return n**7 - 7*n**6 + 21*n**5 - 35*n**4 + 35*n**3 - 21*n**2 + 7*n**1 - n**0


x = list(np.arange(0.998, 1, 0.0001))
y = [f(i) for i in x]
plt.plot(x, y)
plt.title("Method 2")
plt.show()