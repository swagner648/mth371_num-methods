import math


def xdiv(x, a, base):
    v = 0
    q = 0
    r = 0
    t = math.floor(base / a)
    u = base - a * t
    print("-------------------------------")
    print("r:", r, " t:", t, " u:", u)
    for k in range(0, len(x)):
        print("loop ----------------")
        print("r:", r, " v:", v, " q:", q, " x:", x)
        v = x[k] + r * u
        q = math.floor(v / a)
        x[k] = q + r * t
        r = v - a * q
        print("r:", r, " v:", v, " q:", q, " x:", x)


x = [7, 8, 2, 4, 1, 2, 4]
a = 2
base = 10**7
xdiv(x, a, base)