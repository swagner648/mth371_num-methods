import numpy as np


def gradient_descent(F, dF, x_0, dt, max_iter):
    i = 1
    while i < max_iter:
        x_0 = x_0 + dt * dF(x_0)
        i += 1
    return x_0


def lsr(A, b, x_0, dt, max_iter):
    print(b)
    F = lambda x: np.linalg.norm(np.dot(A, x) - b) ** 2
    dF = lambda x: 2 * np.dot(np.transpose(A), (np.dot(A, x) - b))
    return gradient_descent(F, dF, x_0, dt, max_iter)


def massey(point_diff, dt, max_iter):
    n = len(point_diff)
    A = [[-1 for i in range(n)] for i in range(n)]
    for i in range(n):
        A[i][i] = n - 1
    A.append([1 for i in range(n)])
    A = np.array(A)
    print(A)
    point_diff.append(0)
    return lsr(A, np.array(point_diff), np.zeros(n), dt, max_iter)

# Manchester City: 1.7  1
# Liverpool: 1.3        3
# Juventus: 1.4         2
# Real Madrid: 1.3      3
# Chelsea: 0.8          7
# Bayern Munich: 1.7    1
# Atletico Madrid: 0.9  6
# Tottenham: 1.1        4
# Manchester Utd: 1.1   4
# Napoli: 1.0           5
# Barcelona: 1.7        1
# Roma: 0.6             9
# Valencia: 0.7         8
ranks = massey([1.7, 1.3, 1.4, 1.3, 0.8, 1.7, 0.9, 1.1, 1.1, 1.0, 1.7, 0.6, 0.7], 0.0000001, 100000)
print(ranks)
print(sorted(ranks))