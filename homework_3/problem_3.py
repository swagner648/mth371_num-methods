import pandas as pd
import math


def newton_method(x, f, der_f, sol, eps, ans, v, err):
    v.append(x)
    err.append(abs(ans - x))
    if abs(f(x) - sol) < eps:
        # print(pd.DataFrame({'values': v, 'error': err}))
        return x
    return newton_method(x - f(x) / der_f(x), f, der_f, sol, eps, ans, v, err)


def function(x):
    return math.tan(x)


