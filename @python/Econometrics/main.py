import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

x = np.array([
    [4, 5, 5],
    [2, 1, 3],
    [3, 5, 1]
])

y = np.array([
    [9, 5, 5],
    [7, 5, 3],
    [4, 2, 6]
])

m1 = x @ y

if __name__ == "__main__":
    print(m1)
    print(m1.T)
    print(np.linspace(0, 10, 6))
    print(norm.pdf(1))