import sys
import numpy as np

input = sys.stdin.readline
# h: height, w: width
h, w, n = map(int, input().split())
a, b = np.array([]), np.array([])

for i in range(n):
    ai, bi = map(int, input().split())
    a = np.append(a, ai)
    b = np.append(b, bi)
minh = min(a)
minw = min(b)
a = a - minh
b = b - minh




if __name__ == '__main__':
    print(a, b)