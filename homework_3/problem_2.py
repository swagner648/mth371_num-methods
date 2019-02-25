import pandas as pd


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
        # print(pd.DataFrame({'values': v, 'error': err}))      # Print iterations and error
        return x
    return newton_method(x - f(x) / der_f(x), f, der_f, sol, eps, ans, v, err)


def secant_method(a, b, f, sol, eps, ans, v, err):
    v.append(a)
    err.append(abs(ans - a))
    if abs(f(a) - sol) < eps:
        # print(pd.DataFrame({'values': v, 'error': err}))      # Print iterations and error
        return a
    return secant_method(b, a - f(a) * (a - b) / (f(a) - f(b)), f, sol, eps, ans, v, err)


def linear_interpolation(a, b, f, sol):
    return (b * f(a) - a * f(b) + a * sol - b * sol) / (f(a) - f(b))


def function(x):
    return x ** 3 - 2


def der_function(x):
    return 3 * x ** 2


solution = 1.2599210498948732
values = []
error = []
print("Bisection method:\t\t", bisection_method(1, 2, function, 0, 2 ** -52, solution, values, error))
print("Newton method:\t\t\t", newton_method(1, function, der_function, 0, 2 ** -52, solution, values, error))
print("Secant method:\t\t\t", secant_method(1, 2, function, 0, 2 ** -52, solution, values, error))
print("Linear interpolation:\t", linear_interpolation(1, 2, function, 0))
