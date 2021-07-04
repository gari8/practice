import numpy as np

n, k = map(int, input().split())
a_list = list(map(int, input().split()))


def deliver():
    q = k // n
    mod = k % n
    dist = k - n
    tmp = list(np.argsort(a_list))
    if dist > 0:
        for i in range(n):
            mark = tmp.index(i)
            if mod - mark > 0:
                print(q + 1)
            else:
                print(q)
    else:
        tmp = tmp[:k]
        for i in range(n):
            if i in tmp:
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    deliver()
