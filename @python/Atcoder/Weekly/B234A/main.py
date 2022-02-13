import sys

input = sys.stdin.readline
t = int(input())


def func(x):
    return pow(x, 2) + 2 * x + 3


if __name__ == '__main__':
    print(func(func(func(t) + t) + func(func(t))))
