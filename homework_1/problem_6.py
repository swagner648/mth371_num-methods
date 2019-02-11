import matplotlib.pyplot as plt


def threenplus1(n):
    vector_n = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        vector_n.append(n)
    return vector_n


for n in range(2, 11):
    plt.plot(threenplus1(n), label=str(n))
plt.title("threenplus1(2:10)")
plt.legend()
plt.show()
