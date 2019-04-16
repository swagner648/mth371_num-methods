import numpy as np, math, matplotlib.pyplot as plt


# trapezoid rule
def trap(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n)
    sum = 0
    for i in range(0, n - 1):
        sum += h * (f(x[i]) + f(x[i + 1])) / 2
    return sum


def simpson(f, a, b, n):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, n // 2 + 1):
        k += 4 * f(x)
        x += 2 * h
    x = a + 2 * h
    for i in range(1, n // 2):
        k += 2 * f(x)
        x += 2 * h
    return (h / 3) * (f(a) + f(b) + k)


print("\na)")
print("True:", 2.0)
print("Trapezoid Rule:",
      trap(lambda x: math.sin(x), 0, math.pi, 100000))
print("Simpson's Rule:",
      simpson(lambda x: math.sin(x), 0, math.pi, 100000))

print("\nb)")
print("True: log(4) - 3/4")
print("Trapezoid Rule:",
      trap(lambda x: x * math.log(x), 1, 2, 100000))
print("Simpson's Rule:",
      simpson(lambda x: x * math.log(x), 1, 2, 100000))

print("\nc)")
print("True: log(2)/2")
print("Trapezoid Rule:",
      trap(lambda x: math.tan(x), 0, math.pi / 4, 100000))
print("Simpson's Rule:",
      simpson(lambda x: math.tan(x), 0, math.pi / 4, 100000))

print("\nd)")
print("True: 2/3")
print("Trapezoid Rule:", trap(lambda x: x ** 0.5, 0, 1, 100000))
print("Simpson's Rule:", simpson(lambda x: x ** 0.5, 0, 1, 100000))

print("\n\nProblem 2:")
print("Wolfram Alpha:", 0.3474001726572478)
print("Trapezoid Rule:", trap(lambda x: math.sin(x + math.exp(x)), 0, 8, 100000))
print("Simpson's Rule:", simpson(lambda x: math.sin(x + math.exp(x)), 0, 8, 100000))

x = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
y = []
for n in x:
    y.append(simpson(lambda x: math.sin(x), 0, math.pi, n))
plt.plot(x, y)
plt.show()

# APP_ID = 'JQ66GR-QQHLQWHPT7'
# client = wolframalpha.Client(app_id=APP_ID)
# # res = client.query('integrate from 0 to 8 sin(x+e^x)dx')
# res = client.query('2 + 2')
# # print("Wolfralpha:", res)