import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def euler_sys(f, a, b, y_0, n=None, dt=0.001):
    """
    Find ODE approximation of differential system using forward euler method.

    :param f: function whose parameter is an n-length vector and which returns an n-length vector
    :param a: initial time
    :param b: final time
    :param y_0: initial y-values
    :param n: default=None manually set how many iterations to conduct
    :param dt: default=0.001 manually set dt value

    :return: order-length list of n-length list of points
        [[x11, x12, x13, ..., x1n],
         [x21, x22, x23, ..., x2n],
         [ | ,  | ,  | , ...,  | ],
         [xm1, xm2, xm3, ..., xmn]]
    """

    order = len(y_0)
    data = [[] for _ in range(order + 1)]

    if n is not None:
        time = np.linspace(a, b, n)
        dt = (b - a) / (n - 1)
    else:
        time = np.linspace(a, b, int((b - a) / dt) + 1)

    for t in time:
        data[0].append(t)
        for i in range(0, order):
            data[i + 1].append(y_0[i])
        y_0 = [i + dt * j for i, j in zip(y_0, f(t, y_0))]

    return data


def central_diff(f, a, b, y_0, n=None, dt=0.001):
    """
    Find ODE approximation of differential system using central difference formula. Forward euler method
    is used to find the first approximation.

    :param f: function whose parameter is an n-length vector and which returns an n-length vector
    :param a: initial time
    :param b: final time
    :param y_0: initial y-values
    :param n: default=None manually set how many iterations to conduct
    :param dt: default=0.001 manually set dt value

    :return: order-length list of n-length list of points
        [[x11, x12, x13, ..., x1n],
         [x21, x22, x23, ..., x2n],
         [ | ,  | ,  | , ...,  | ],
         [xm1, xm2, xm3, ..., xmn]]
    """

    order = len(y_0)
    data = [[] for _ in range(order + 1)]

    if n is not None:
        time = np.linspace(a, b, n)
        dt = (b - a) / (n - 1)
    else:
        time = np.linspace(a, b, int((b - a) / dt) + 1)

    data[0].append(time[0])
    for i in range(0, order):
        data[i + 1].append(y_0[i])
    y_0 = [i + dt * j for i, j in zip(y_0, f(time[0], y_0))]

    for t in time[1:]:
        data[0].append(t)
        for i in range(0, order):
            data[i + 1].append(y_0[i])
        y_prev = [d[-2] for d in data[1:]]
        y_0 = [i + 2 * dt * j for i, j in zip(y_prev, f(t, y_0))]

    return data


def plot_sys(supertitle, data):
    fig = plt.figure(figsize=(20, 5))
    plot_eqn(fig, 141, [data[1], data[2], data[0]], 't vs y vs x', grid=True)
    plot_eqn(fig, 142, [data[1], data[2]], 'y vs x', xlim=(-5, 5), ylim=(-5, 5), grid=True)
    plot_eqn(fig, 143, [data[0], data[2]], 'y vs t', xlim=(0, 60), ylim=(-5, 5), grid=True)
    plot_eqn(fig, 144, [data[0], data[1]], 'x vs t', xlim=(0, 60), ylim=(-5, 5), grid=True)
    fig.suptitle(supertitle)
    plt.show()


def plot_field(supertitle, data):
    fig, ax = plt.subplots(figsize=(10, 10))
    for path in data:
        plot_eqn(ax, 1, [path[1], path[2]], None, xlim=(0, 10), ylim=(0, 10))
    fig.suptitle(supertitle)
    plt.show()


def plot_eqn(fig, pos, data, title, xlim=None, ylim=None, grid=False):
    if pos == 1:
        fig.plot(data[0], data[1])
    else:
        if len(data) == 2:
            ax = fig.add_subplot(pos)
            ax.plot(data[0], data[1])
        elif len(data) == 3:
            ax = fig.add_subplot(pos, projection='3d')
            ax.plot3D(data[0], data[1], data[2])
        else:
            raise TypeError('Input data must be either 2 or 3-dimensional.')
        ax.set_title(title)
        if xlim is not None:
            ax.set_xlim(xlim)
        if ylim is not None:
            ax.set_ylim(ylim)
        if grid:
            ax.grid()


# plot_sys('Euler Act 1', euler_sys(lambda t, y: [-0.2 * y[1], 0.8 * y[0]], 0, 60, [2, 0], dt=0.0005))
# plot_sys('Euler Act 2', euler_sys(lambda t, y: [-0.2 * y[1], 0.8 * y[0] - 0.1 * y[1]], 0, 60, [2, 0], dt=0.0005))
# plot_sys('Euler Act 3', euler_sys(lambda t, y: [-0.2 * (y[1] - 2), 0.8 * (y[0] - 2)], 0, 60, [2, 0], dt=0.0005))
#
# plot_sys('Central Difference Act 1', central_diff(lambda t, y: [-0.2 * y[1], 0.8 * y[0]], 0, 60, [2, 0], dt=0.0005))


def course1(t, y):
    dx = 0.4 * y[0] - 0.08 * y[0] ** 2 - 0.04 * y[0] * y[1]
    dy = 0.2 * y[1] - 0.04 * y[1] ** 2 - 0.02 * y[0] * y[1]
    return [dx, dy]


plot_field('Cannibals First Course', [euler_sys(course1, 0, 60, [0.01, 0.3], dt=0.0005),
                                      euler_sys(course1, 0, 60, [0.01, 10], dt=0.0005),
                                      euler_sys(course1, 0, 60, [6, 10], dt=0.0005),
                                      euler_sys(course1, 0, 60, [10, 6], dt=0.0005),
                                      euler_sys(course1, 0, 60, [10, 2.2], dt=0.0005),
                                      euler_sys(course1, 0, 60, [10, 0.2], dt=0.0005)])


def course2(t, y):
    dx = 0.4 * y[0] - 0.08 * y[0] ** 2 - 0.02 * y[0] * y[1]
    dy = 0.2 * y[1] - 0.04 * y[1] ** 2 - 0.05 * y[0] * y[1]
    return [dx, dy]


plot_field('Cannibals Second Course', [euler_sys(course2, 0, 60, [0.01, 0.3], dt=0.0005),
                                       euler_sys(course2, 0, 60, [0.01, 10], dt=0.0005),
                                       euler_sys(course2, 0, 60, [1.8, 10], dt=0.0005),
                                       euler_sys(course2, 0, 60, [4.8, 10], dt=0.0005),
                                       euler_sys(course2, 0, 60, [10, 7], dt=0.0005),
                                       euler_sys(course2, 0, 60, [10, 3], dt=0.0005)])
