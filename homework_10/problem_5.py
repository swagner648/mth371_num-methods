def pprint(A):
    max_len = max([max([len(str(i)) for i in j]) for j in A])
    for i in range(0, len(A)):
        line = ""
        for j in range(0, len(A[0])):
            line += str(A[i][j]).ljust(max_len + 2)
        print(line)


def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


def inverse(A):
    try:
        A_i = copy.deepcopy(A)
        for j in range(0, len(A[0])):
            e_j = [0 for i in range(len(A))]
            e_j[j] = 1
            sys = [A[i] + [e_j[i]] for i in range(len(A))]
            x_j = gauss(sys)
            for i in range(len(x_j)):
                A_i[i][j] = x_j[i]
        return A_i
    except ZeroDivisionError:
        warnings.warn("Input matrix in not invertible.", Warning)


if __name__ == "__main__":
    import copy, warnings, numpy as np, time
    from numpy.linalg import inv
    from fractions import Fraction

    for n in [5]:
        print('\n', str(n) + ' by ' + str(n), 'Hilbert Matrix Inversion')
        print('-----------------------------------------------------')

        H = [[Fraction(1, i+j+1) for j in range(n)] for i in range(n)]

        print('My inverse() method without converting H to np.array using Fractions:')
        start = time.time()
        pprint(inverse(H))
        print('Time:', time.time() - start, '\n')

        H = [[1 / (i + j + 1) for j in range(n)] for i in range(n)]

        print('My inverse() method without converting H to np.array using Doubles:')
        start = time.time()
        inverse(H)
        print('Time:', time.time() - start, '\n')

        print('My inverse() method when converting H to np.array using Doubles:')
        start = time.time()
        np.array(inverse(H))
        print('Time:', time.time() - start, '\n')

        print('NumPy inv() method using Doubles:')
        start = time.time()
        inv(H)
        print('Time:', time.time() - start, '\n')

        np.array(inverse(H)) * np.array(H)