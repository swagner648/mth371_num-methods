
def fibonacci(n):
    if n is 0:
        return []
    vec_fib = [0, 1]
    for i in range(2, n + 1):
        vec_fib.append(vec_fib[i - 1] + vec_fib[i - 2])
    return vec_fib[1:]


fib = fibonacci(40)
print(fib)
phi = []
for i in range(39):
    phi.append(round(fib[i + 1] / fib[i], 10))
print(phi[-5:-1])
