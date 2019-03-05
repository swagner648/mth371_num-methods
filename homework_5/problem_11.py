import numpy as np
import numpy.polynomial.polynomial as poly
import math
import warnings


def newton_compute(x, i, j):
    p = 1
    for k in range(0, j):
        p *= (x[i] - x[k])
    return p


def newton_form_coef(x, y):
    n = len(x)
    coef = [[0 for x in range(n)] for y in range(n)]
    p = 1
    for i in range(0, n):
        for j in range(0, n):
            if j == 0:
                coef[i][j] = 1
            elif j <= i:
                coef[i][j] = newton_compute(x, i, j)
    return np.linalg.solve(coef, y)


def newton_div_coef(x, y):
    coef = y
    n = len(x)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    print(coef)
    return coef


def lagrange_coef(x, y):
    n = len(x)
    l = [1] * n
    coef = [0] * n
    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                l[i] *= 1 / (x[i] - x[j])
                coef[i] = y[i] * l[i]
    return coef


def horner_eval(coef, x):
    coef = coef[::-1]
    p = coef[-1]
    i = len(coef) - 2
    while i >= 0:
        p = p * x + coef[i]
        i -= 1
    return p


def res_eval(p, x, y, k):
    norm = 0
    for i, sample_point in enumerate(x):
        tmp = horner_eval(p, sample_point) - y[i]
        if k == 0:
            prev = abs(tmp)  # Swap for the max
            if prev > norm:
                norm = tmp
        elif k == 1:
            norm += abs(tmp)
        else:
            norm += abs(tmp) ** 2
    return norm / (len(x))


def run(f, lb, ub, letter):
    x_points = [i for i in np.arange(lb, ub, (ub - lb) / 201)]
    y_points = [f(i) for i in x_points]

    nfc = newton_form_coef(x_points, y_points)
    ndc = newton_div_coef(x_points, y_points)
    lc = lagrange_coef(x_points, y_points)

    polyfit = poly.polyfit(x_points, y_points, 200)

    x_points = [i for i in np.arange(lb, ub, (ub - lb) / 1001)]
    y_points = [f(i) for i in x_points]
    print(f"-----------------------------------\nResults for ({letter}):")
    print("nfc:\t", res_eval(nfc, x_points, y_points, 0))
    print("ndc:\t", res_eval(ndc, x_points, y_points, 0))
    print("lc:\t\t", res_eval(lc, x_points, y_points, 0))
    print("polyfit:", res_eval(polyfit, x_points, y_points, 0))


# run(math.sin, 0, math.pi, 'a')
# run(math.cos, 0, math.pi, 'b')
# run(math.log, 0.5, 2, 'c')
# run(math.exp, 0, 2, 'd')

newton_div_coef([0, 1, -1], [1, 3, 1])