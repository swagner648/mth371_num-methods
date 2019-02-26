import pandas as pd


def fixed_point_iteration(b, f, eps):
    a = b - 1
    while abs(b - a) > eps:
        temp = b
        b = a
        a = f(temp)
    return a


# a
def function_a(x):
    return (3 - x - 2 * x * x) ** 0.25


print("a:", fixed_point_iteration(0.5, function_a, 2 ** -52))


# b
def function_b(x):
    return (3 * x ** 4 + 2 * x ** 2 + 3) / (4 * x ** 3 + 4 * x - 1)


# print("b:", fixed_point_iteration(0.5, function_b, 2 ** -52))     # exceeds reasonable computation time


# c
def secant_method(a, b, f, sol, eps, ans, v, err):
    v.append(a)
    err.append(abs(ans - a))
    if abs(f(a) - sol) < eps:
        # print(pd.DataFrame({'values': v, 'error': err}))  # Print iterations and error
        return a
    return secant_method(b, a - f(a) * (a - b) / (f(a) - f(b)), f, sol, eps, ans, v, err)


def function_c(x):
    return x ** 4 + 2 * x ** 2 - x - 3


print("c:", secant_method(0.5, 2, function_c, 0, 2 ** -52, 0, [], []))


# d
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
        # print(df)      # Print iterations and error and rate of convergence
        return x
    return newton_method(x - f(x) / der_f(x), f, der_f, sol, eps, ans, v, err)


def der_function_c(x):
    return 4 * x ** 3 + 4 * x - 1


print("d:", newton_method(0.5, function_c, der_function_c, 0, 2 ** -52, 0, [], []))
