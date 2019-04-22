import operator as op, numpy as np, pandas as pd, math
from functools import reduce


def trap(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n)
    sum = 0
    for i in range(0, n - 1):
        sum += h * (f(x[i]) + f(x[i + 1])) / 2
    return sum


def simpson(f, a, b, n):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, n // 2 + 1):
        k += 4 * f(x)
        x += 2 * h
    x = a + 2 * h
    for i in range(1, n // 2):
        k += 2 * f(x)
        x += 2 * h
    return (h / 3) * (f(a) + f(b) + k)


def nCr(n, r):
    r = min(r, n - r)
    num = reduce(op.mul, range(n, n - r, -1), 1)
    den = reduce(op.mul, range(1, r + 1), 1)
    return num / den


def bisect(f, a, b, eps):
    midpoint = (a + b) / 2
    if abs(f(midpoint) - 0) < eps:
        return midpoint
    if (f(midpoint) > 0 and f(a) > 0) or (f(midpoint) < 0 and f(a) < 0):
        return bisect(f, midpoint, b, eps)
    else:
        return bisect(f, a, midpoint, eps)


def P(n):
    return lambda x: sum(nCr(n, k) * nCr(n + k, k) * ((x - 1) / 2) ** k for k in range(0, n + 1))


def find_roots(Pn, n, a, b):
    roots = []
    dt = 1
    eps = 10 ** -10
    while len(roots) < n:
        roots = []
        dt *= 0.5
        Pn_prime = lambda p: (Pn(p + 2 ** -11) - Pn(p - 2 ** -11)) / (2 ** -10)
        for p in np.linspace(a, b, int((b - a) / dt)):
            if np.sign(Pn(p)) != np.sign(Pn(p + dt)):
                roots.append(bisect(Pn, p, p + dt, eps))
            if np.sign(Pn_prime(p)) != np.sign(Pn_prime(p + dt)):
                potential_root = bisect(Pn_prime, a, b, eps)
                if abs(Pn(potential_root)) < eps:
                    roots.append(potential_root)
    return roots


def find_weights(Pn, roots):
    return [2 / ((1 - p ** 2) * ((Pn(p + 2 ** -11) - Pn(p - 2 ** -11)) / (2 ** -10)) ** 2) for p in roots]


def gaussian_quadrature(n, a=-1, b=1):
    Pn = P(n)
    roots = find_roots(Pn, n, a, b)
    weights = find_weights(Pn, roots)
    # roots = [round(r, 6) for r in roots]
    # weights = [round(w, 6) for w in weights]
    return roots, weights


def integrate(f, a, b, quadrature):
    points = quadrature[0]
    weights = quadrature[1]
    return (b - a) / 2 * sum(w * f((b - a) / 2 * x + (b + a) / 2) for w, x in zip(weights, points))


# print("\n1:\n", pd.DataFrame({'roots': gaussian_quadrature(1)[0], 'weights': gaussian_quadrature(1)[1]}))
# print("\n2:\n", pd.DataFrame({'roots': gaussian_quadrature(2)[0], 'weights': gaussian_quadrature(2)[1]}))
# print("\n3:\n", pd.DataFrame({'roots': gaussian_quadrature(3)[0], 'weights': gaussian_quadrature(3)[1]}))
# print("\n4:\n", pd.DataFrame({'roots': gaussian_quadrature(4)[0], 'weights': gaussian_quadrature(4)[1]}))
# print("\n5:\n", pd.DataFrame({'roots': gaussian_quadrature(5)[0], 'weights': gaussian_quadrature(5)[1]}))
# print("\n6:\n", pd.DataFrame({'roots': gaussian_quadrature(6)[0], 'weights': gaussian_quadrature(6)[1]}))
# print("\n7:\n", pd.DataFrame({'roots': gaussian_quadrature(7)[0], 'weights': gaussian_quadrature(7)[1]}))
# print("\n8:\n", pd.DataFrame({'roots': gaussian_quadrature(8)[0], 'weights': gaussian_quadrature(8)[1]}))
# print("\n9:\n", pd.DataFrame({'roots': gaussian_quadrature(9)[0], 'weights': gaussian_quadrature(9)[1]}))
# print("\n10:\n", pd.DataFrame({'roots': gaussian_quadrature(10)[0], 'weights': gaussian_quadrature(10)[1]}))

print("\na) \t1 / x ** 0.5")
print("Actual:\t\t\t\t", 1.1715728752538099)
print("Gaussian quadrature:", integrate(lambda x: 1 / x ** 0.5, 2, 4, gaussian_quadrature(5)))
print("Trapezoid rule:\t\t", trap(lambda x: 1 / x ** 0.5, 2, 4, 1000))
print("Simpson's rule:\t\t", simpson(lambda x: 1 / x ** 0.5, 2, 4, 1000))
print("\nb) \tsin(x)")
print("Actual:", 2.0)
print("Gaussian quadrature:", integrate(lambda x: math.sin(x), 0, math.pi, gaussian_quadrature(5)))
print("Trapezoid rule:\t\t", trap(lambda x: math.sin(x), 0, math.pi, 1000))
print("Simpson's rule:\t\t", simpson(lambda x: math.sin(x), 0, math.pi, 1000))
print("\na) \t1 / (1 + x ** 2)")
print("Actual:\t\t\t\t", 2.9919656053766884)
print("Gaussian quadrature:", integrate(lambda x: 1 / (1 + x ** 2), -10, 20, gaussian_quadrature(5)))
print("Trapezoid rule:\t\t", trap(lambda x: 1 / (1 + x ** 2), -10, 20, 1000))
print("Simpson's rule:\t\t", simpson(lambda x: 1 / (1 + x ** 2), -10, 20, 1000))
