import numpy as np, matplotlib.pyplot as plt, math
from mpl_toolkits.mplot3d import Axes3D


def euler_sys(f, a, b, y_0, n=None, dt=0.001):
    """
    Find euler approximation of differential system.

    :param f: function whose parameter is an n-length vector and which returns an n-length vector
    :param a: initial time
    :param b: final time
    :param y_0: initial y-values
    :param n: default=None manaully set how many iterations to conduct
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


def plot_sys(suptitle, data):
    fig = plt.figure(figsize=(20, 5))
    plot_eqn(fig, 141, [data[1], data[2], data[0]], 't vs y vs x', grid=True)
    plot_eqn(fig, 142, [data[1], data[2]], 'y vs x', xlim=(-5, 5), ylim=(-5, 5), grid=True)
    plot_eqn(fig, 143, [data[0], data[2]], 'y vs t', xlim=(0, 60), ylim=(-5, 5), grid=True)
    plot_eqn(fig, 144, [data[0], data[1]], 'x vs t', xlim=(0, 60), ylim=(-5, 5), grid=True)
    fig.suptitle(suptitle)
    plt.show()


def plot_eqn(fig, pos, data, title, xlim=None, ylim=None, grid=False):
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
    return ax


plot_sys('Act 1', euler_sys(lambda t, y: [-0.2 * y[1], 0.8 * y[0]], 0, 60, [2, 0], dt=0.0005))
plot_sys('Act 2', euler_sys(lambda t, y: [-0.2 * y[1], 0.8 * y[0] - 0.1 * y[1]], 0, 60, [2, 0], dt=0.0005))
plot_sys('Act 3', euler_sys(lambda t, y: [-0.2 * (y[1] - 2), 0.8 * (y[0] - 2)], 0, 60, [2, 0], dt=0.0005))

