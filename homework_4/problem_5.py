def fixed_point_iteration(b, f, eps):
    a = b - 1
    while abs(b - a) > eps:
        print(abs(b - a), a, b)
        temp = b
        b = a
        a = f(temp)
    return a


def function(x):
    return 0.5 * (x + 9 / x)


print(fixed_point_iteration(4, function, 2 ** -52))