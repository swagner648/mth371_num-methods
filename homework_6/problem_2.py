import numpy as np
from math import sqrt
import matplotlib.pyplot as plt


def newton_form_coef(x, y):
    return np.linalg.solve(np.vander(x), y)


def poly_coefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

        The coefficients must be in ascending order (``x**0`` to ``x**o``).
        """
    o = len(coeffs)
    print(f'# This is a polynomial of order {ord}.')
    y = 0
    for i in range(o):
        y += coeffs[i] * x ** i
    return y


def linear_spline(x, y, t):
    n = 0
    while x[n] <= t:
        n += 1
    return y[n - 1] * (t - x[n]) / (x[n - 1] - x[n]) + y[n] * (t - x[n - 1]) / (x[n] - x[n - 1])


def cubic_interp1d(x0, x, y):
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
    Li[0] = sqrt(2 * xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0  # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size - 1, 1):
        Li_1[i] = xdiff[i - 1] / Li[i - 1]
        Li[i] = sqrt(2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = size - 1
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = sqrt(2 * xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])
    Bi = 0.0  # natural boundary
    z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    # solve [L.T][x] = [y]
    i = size - 1
    z[i] = z[i] / Li[i]
    for i in range(size - 2, -1, -1):
        z[i] = (z[i] - Li_1[i - 1] * z[i + 1]) / Li[i]

    # find index
    index = x.searchsorted(x0)
    np.clip(index, 1, size - 1, index)

    xi1, xi0 = x[index], x[index - 1]
    yi1, yi0 = y[index], y[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0 / (6 * hi1) * (xi1 - x0) ** 3 + \
         zi1 / (6 * hi1) * (x0 - xi0) ** 3 + \
         (yi1 / hi1 - zi1 * hi1 / 6) * (x0 - xi0) + \
         (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x0)
    return f0


def function(x):
    return 1 / (1 + x ** 2)


x = np.linspace(-5, 5, 11)
y = [function(i) for i in x]
x_new = np.linspace(-5, 5, 201)

plt.scatter(x, y)
plt.plot(x_new, poly_coefficients(x_new, newton_form_coef(x, y)[::-1]))
plt.plot(x_new, [function(i) for i in x_new])
plt.ylim(-0.5, 2)
plt.title('Newton Int')
plt.show()

plt.scatter(x, y)
plt.plot(x, y)
plt.plot(x_new, [function(i) for i in x_new])
plt.ylim(-0.5, 2)
plt.title('Linear Spline')
plt.show()

plt.scatter(x, y)
plt.plot(x_new, cubic_interp1d(x_new, x, y))
plt.plot(x_new, [function(i) for i in x_new])
plt.ylim(-0.5, 2)
plt.title('Cubic Spline')
plt.show()
