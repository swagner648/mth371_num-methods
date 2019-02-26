import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np


def bisection_method(a, b, f, sol, eps, ans, v, err):
    midpoint = (a + b) / 2
    v.append(midpoint)
    err.append(abs(ans - midpoint))
    if abs(f(midpoint) - sol) < eps:
        # print(pd.DataFrame({'values': v, 'error': err}))      # Print iterations and error
        return midpoint
    if f(midpoint) > sol:
        return bisection_method(a, midpoint, f, sol, eps, ans, v, err)
    else:
        return bisection_method(midpoint, b, f, sol, eps, ans, v, err)


def newton_method(x, f, der_f, sol, eps, ans, v, err):
    v.append(x)
    err.append(abs(ans - x))
    if abs(f(x) - sol) < eps:
        df = pd.DataFrame({'values': v, 'error': err})
        df['roc'] = 0.0
        for i in range(1, len(df.values) - 1):
            num = abs(df.error[i + 1])
            den = abs(df.error[i])
            df.roc[i - 1] = num / den
        plt.plot(df['error'])
        # print(df)      # Print iterations and error and rate of convergence
        return x
    return newton_method(x - f(x) / der_f(x), f, der_f, sol, eps, ans, v, err)


def secant_method(a, b, f, sol, eps, ans, v, err):
    v.append(a)
    err.append(abs(ans - a))
    if abs(f(a) - sol) < eps:
        print(pd.DataFrame({'values': v, 'error': err}))  # Print iterations and error
        return a
    return secant_method(b, a - f(a) * (a - b) / (f(a) - f(b)), f, sol, eps, ans, v, err)


def linear_interpolation(a, b, f, sol):
    return (b * f(a) - a * f(b) + a * sol - b * sol) / (f(a) - f(b))


def function(x):
    return x ** 3 - 2


def der_function(x):
    return 3 * x ** 2


def tan_function(x):
    return math.tan(x) - x


def sin_function(x):
    return math.sin(x)


def der_sin_function(x):
    return math.cos(x)


def sin2_function(x):
    return math.sin(x) * math.sin(x)


def der_sin2_function(x):
    return math.sin(2 * x)


solution = 1.2599210498948732
values = []
error = []
print("Bisection method:\t\t", bisection_method(1, 2, function, 0, 2 ** -52, solution, values, error))
print("Newton method:\t\t\t", newton_method(1, function, der_function, 0, 2 ** -52, solution, values, error))
print("Secant method:\t\t\t", secant_method(1, 2, function, 0, 2 ** -52, solution, values, error))
print("Linear interpolation:\t", linear_interpolation(1, 2, function, 0))

for i in np.arange(-math.pi / 2, 9 * math.pi + math.pi / 2, math.pi):
    print("Bisection method:\t\t", bisection_method(i, i + math.pi, tan_function, 0, 2 ** -39, 0, values, error))

plt.figure(figsize=(10, 10))

print("Newton method:\t\t\t",
      newton_method(3.14, sin_function, der_sin_function, 0, 2 ** -52, math.pi, values, error))
print("Newton method:\t\t\t",
      newton_method(3.14, sin2_function, der_sin2_function, 0, 2 ** -52, math.pi, values, error))
plt.legend()
plt.show()
