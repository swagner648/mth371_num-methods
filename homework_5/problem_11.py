import numpy as np
import numpy.polynomial.polynomial as poly
import math
import warnings


def newton_form_coef(x, y):
    return np.linalg.solve(np.vander(x), y)


def newton_div_coef(x, y):
    coef = y
    n = len(x)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef


def lagrange_coef(x, y):
    n = len(x)
    Lj = np.array([np.array([0.0 for i in range(n)]) for i in range(n)])

    for i in range(0, n):
        m = 1.0
        c = 1.0
        for k in range(0, n):
            if k != i and x[k] != x[i]:
                c = np.convolve(c, [1, -x[k]])
                m = m * (x[i] - x[k]) ** -1
        Lj[i, :] = m * c
    return np.matmul(y, Lj)


def horner_eval(coef, x):
    p = coef[0]
    for i in range(1, len(coef)):
        p = p * x + coef[i]
    return p


def res_eval(p, x, y, k):
    norm = 0
    for i, sample_point in enumerate(x):
        tmp = horner_eval(p, sample_point) - y[i]
        if k == 0:
            if abs(tmp) > norm:
                norm = tmp
        elif k == 1:
            norm += abs(tmp)
        else:
            norm += abs(tmp) ** 2
    return norm / (len(x))


def run(f, lb, ub, letter):
    x_points = [i for i in np.linspace(lb, ub, 201)]
    y_points = [f(i) for i in x_points]

    nfc = newton_form_coef(x_points, y_points)
    ndc = newton_div_coef(x_points, y_points)
    lc = lagrange_coef(x_points, y_points)

    polyfit = poly.polyfit(x_points, y_points, 200)[::-1]

    x_points = [i for i in np.linspace(lb, ub, 1001)]
    y_points = [f(i) for i in x_points]
    print(f"-----------------------------------\nResults for ({letter}):")
    print("L  Algthm \t Residual")
    print("0  nfc:\t\t", res_eval(nfc, x_points, y_points, 0))
    # print("0  ndc:\t\t", res_eval(ndc, x_points, y_points, 0))
    print("0  lc:\t\t", res_eval(lc, x_points, y_points, 0))
    print("0  polyfit:\t", res_eval(polyfit, x_points, y_points, 0))
    print("1  nfc:\t\t", res_eval(nfc, x_points, y_points, 1))
    # print("1  ndc:\t\t", res_eval(ndc, x_points, y_points, 1))
    print("1  lc:\t\t", res_eval(lc, x_points, y_points, 1))
    print("1  polyfit:\t", res_eval(polyfit, x_points, y_points, 1))
    print("2  nfc:\t\t", res_eval(nfc, x_points, y_points, 2))
    # print("2  ndc:\t\t", res_eval(ndc, x_points, y_points, 2))
    print("2  lc:\t\t", res_eval(lc, x_points, y_points, 2))
    print("2  polyfit:\t", res_eval(polyfit, x_points, y_points, 2))


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    run(math.sin, 0, 2 * math.pi, 'a')
    run(math.cos, 0, 2 * math.pi, 'b')
    run(math.log, 0.5, 2, 'c')
    run(math.exp, 0, 2, 'd')

# print(newton_form_coef([-4, -2, 0], [9, 3, 5]))
# print(newton_div_coef([-4, -2, 0], [9, 3, 5]))
# print(lagrange_coef([-4, -2, 0], [9, 3, 5]))
# print(poly.polyfit([-4, -2, 0], [9, 3, 5], 2)[::-1])
