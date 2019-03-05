import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
import math


def f(x):
    return 1 / (1 + 25 * x ** 2)


a_x = np.linspace(-1, 1, 100)
a_y = [f(i) for i in a_x]
p = np.poly1d(poly.polyfit(a_x, a_y, 10)[::-1])
polyfit = [p(i) for i in a_x]
a_cx = [math.cos(math.pi * i / 10) for i in range(11)]
a_cy = [f(i) for i in a_cx]
cp = np.poly1d(poly.polyfit(a_cx, a_cy, 10)[::-1])
cpolyfit = cp(a_x)

plt.figure(figsize=(15, 15))
plt.plot(a_x, a_y, 'b--', label="Standard Points")
plt.plot(a_cx, a_cy, 'r^', label="Chebyshev Points")
plt.plot(a_x, polyfit, label="Standard Polyfit")
plt.plot(a_x, cpolyfit, label="Chebyshev Polyfit")
plt.title("Polyfit Sample Comparisons")
plt.legend()
plt.show()
