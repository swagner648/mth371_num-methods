import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

plt.figure()
plt.xlim(0, 10)
plt.ylim(0, 10)
data = np.matrix(plt.ginput(10))
col1 = np.array(data[:, 0]).squeeze()
col2 = np.array(data[:, 1]).squeeze()
# print(data, "\ncol1", len(col1), type(col1), "\n", col1, "\ncol2", len(col2), type(col2), "\n", col2)

plt.figure()
plt.xlim(0, 10)
plt.ylim(0, 10)
f = interp1d(col1, col2, fill_value="extrapolate")
f2 = interp1d(col1, col2, 9, fill_value="extrapolate")
plt.plot(col1, col2, "bo")
plt.plot(np.linspace(0, 10, 100), f(np.linspace(0, 10, 100)), "r-")
plt.plot(np.linspace(0, 10, 100), f2(np.linspace(0, 10, 100)), "g--")
plt.show()
