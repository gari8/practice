import math
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))


def gcd_checker(n: int, c: int) -> bool:
    flag = False
    for i in range(n):
        if math.gcd(a[i], c) == 1:
            flag = True
    return flag


if __name__ == '__main__':
    for i in range(m):
        if i != 0 and gcd_checker(n, i):
            print(i)
