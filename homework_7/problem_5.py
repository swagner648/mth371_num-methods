import numpy as np, math, pandas as pd


def inter_poly(x_new, x, y):
    """
        Returns a polynomial for ``x`` values for the ``coeffs`` provided.

        The coefficients must be in ascending order (``x**0`` to ``x**o``).
        """
    coeffs = np.linalg.solve(np.vander(x), y)
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i] * x_new ** i
    return y


def cubic_spline(x_new, x, y):
    """
        Interpolate a 1-D function using cubic splines.
          x0 : a float or an 1d-array
          x : (N,) array_like
              A 1-D array of real/complex values.
          y : (N,) array_like
              A 1-D array of real values. The length of y along the
              interpolation axis must be equal to the length of x.

        Implement a trick to generate at first step the cholesky matrice L of
        the tridiagonal matrice A (thus L is a bidiagonal matrice that
        can be solved in two distinct loops).

        additional ref: www.math.uh.edu/~jingqiu/math4364/spline.pdf
        """
    x = np.asfarray(x)
    y = np.asfarray(y)

    # check if sorted
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # allocate buffer matrices
    Li = np.empty(size)
    Li_1 = np.empty(size - 1)
    z = np.empty(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0] = math.sqrt(2 * xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0  # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size - 1, 1):
        Li_1[i] = xdiff[i - 1] / Li[i - 1]
        Li[i] = math.sqrt(
            2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = size - 1
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = math.sqrt(2 * xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])
    Bi = 0.0  # natural boundary
    z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    # solve [L.T][x] = [y]
    i = size - 1
    z[i] = z[i] / Li[i]
    for i in range(size - 2, -1, -1):
        z[i] = (z[i] - Li_1[i - 1] * z[i + 1]) / Li[i]

    # find index
    index = x.searchsorted(x_new)
    np.clip(index, 1, size - 1, index)

    xi1, xi0 = x[index], x[index - 1]
    yi1, yi0 = y[index], y[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0 / (6 * hi1) * (xi1 - x_new) ** 3 + \
         zi1 / (6 * hi1) * (x_new - xi0) ** 3 + \
         (yi1 / hi1 - zi1 * hi1 / 6) * (x_new - xi0) + \
         (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x_new)
    return f0


def f_prime(x, f, h):
    if h == 0:
        h = math.sqrt(2 ** -1)
    return 1 / (4 * h) * (f(x + 2 * h) - f(x - 2 * h))


def f_double_prime(x, f, h):
    return 1 / (4 * h ** 2) * (f(x + 2 * h) - 2 * f(x) + f(x - 2 * h))


def a(f, x_lb, x_ub, points):
    x = np.linspace(x_lb, x_ub, points)
    y = [f(i) for i in x]
    x_new = np.linspace(x_lb, x_ub, 10 * points)
    poly = inter_poly(x_new, x, y)
    dydx = np.diff(poly) / np.diff(x_new)
    data = [f_prime(i, f, i * math.sqrt(2 ** -1)) for i in x_new]
    error = [i - j for i, j in zip(data, dydx)]
    print("\nError Table for (a)")
    print(pd.DataFrame({'x': x_new[:-1], 'error': error}).sample(
        10).sort_values(by=['x']))


def b(f, x_lb, x_ub, points):
    x = np.linspace(x_lb, x_ub, points)
    y = [f(i) for i in x]
    x_new = np.linspace(x_lb, x_ub, 10 * points)
    spline = cubic_spline(x_new, x, y)
    dydx = np.diff(spline) / np.diff(x_new)
    data = [f_prime(i, f, i * math.sqrt(2 ** -1)) for i in x_new]
    error = [i - j for i, j in zip(data, dydx)]
    print("\nError Table for (b)")
    print(pd.DataFrame({'x': x_new[:-1], 'error': error}).sample(
        10).sort_values(by=['x']))


def c(f, x_lb, x_ub, points):
    x = np.linspace(x_lb, x_ub, points)
    y = [f(i) for i in x]
    dydx = np.diff(y) / np.diff(x)
    x_new = np.linspace(x_lb, x_ub, 10 * points)
    poly = inter_poly(x_new, x[:-1], dydx)
    dydx = np.diff(poly) / np.diff(x_new)
    data = [f_prime(i, f, i * math.sqrt(2 ** -1)) for i in x_new]
    error = [i - j for i, j in zip(data, dydx)]
    print("\nError Table for (c)")
    print(pd.DataFrame({'x': x_new[:-1], 'error': error}).sample(
        10).sort_values(by=['x']))


def d(f, x_lb, x_ub, points):
    x = np.linspace(x_lb, x_ub, points)
    y = [f(i) for i in x]
    dydx = np.diff(y) / np.diff(x)
    x_new = np.linspace(x_lb, x_ub, 10 * points)
    spline = cubic_spline(x_new, x[:-1], dydx)
    dydx = np.diff(spline) / np.diff(x_new)
    data = [f_prime(i, f, i * math.sqrt(2 ** -1)) for i in x_new]
    error = [i - j for i, j in zip(data, dydx)]
    print("\nError Table for (d)")
    print(pd.DataFrame({'x': x_new[:-1], 'error': error}).sample(
        10).sort_values(by=['x']))


print("-----------------------------")
print("Sine Function:")
a(math.sin, 0, math.pi, 21)
b(math.sin, 0, math.pi, 21)
c(math.sin, 0, math.pi, 21)
d(math.sin, 0, math.pi, 21)

print("\n-----------------------------")
print("Runge's Function:")
a(lambda x: 1 / (1 + 25 * x ** 2), -1, 1, 21)
b(lambda x: 1 / (1 + 25 * x ** 2), -1, 1, 21)
c(lambda x: 1 / (1 + 25 * x ** 2), -1, 1, 21)
d(lambda x: 1 / (1 + 25 * x ** 2), -1, 1, 21)
