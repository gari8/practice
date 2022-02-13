import sys
import math

input = sys.stdin.readline
N = int(input())
xy = []

for i in range(N):
    x, y = map(int, input().split())
    xy.append([x, y])


def dist(a, b):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    return math.sqrt(pow(ay - by, 2) + pow(ax - bx, 2))


if __name__ == '__main__':
    max_num = -1
    for i in range(N):
        for j in range(i + 1, N):
            if dist(xy[i], xy[j]) >= max_num:
                max_num = dist(xy[i], xy[j])
    print(max_num)