import operator as op, tensorflow as tf, numpy as np, math
from functools import reduce


def nCr(n, r):
    r = min(r, n - r)
    num = reduce(op.mul, range(n, n - r, -1), 1)
    den = reduce(op.mul, range(1, r + 1), 1)
    return num / den


def P(n):
    return lambda x: sum(nCr(n, k) * nCr(n + k, k) * ((x - 1) / 2) ** k for k in range(0, n + 1))


def gaussian_quadrature(n, a=-1, b=1):
    Pn = P(n)
    points = []
    weights = []
    return points, weights


def integrate(f, quadrature):
    points = quadrature[0]
    weights = quadrature[1]
    return sum(w * f(x) for w, x in zip(weights, points))


print(gaussian_quadrature(2))
