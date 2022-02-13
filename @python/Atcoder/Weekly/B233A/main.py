import math
import sys

input = sys.stdin.readline
X, Y = map(int, input().split())

if __name__ == '__main__':
    dist = Y - X
    ans = math.ceil(dist / 10)
    if ans > 0:
        print(ans)
    else:
        print(0)
