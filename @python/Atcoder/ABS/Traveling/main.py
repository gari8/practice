from collections import deque

n = int(input())

d = deque()
d.append([0, 0, 0])

for _ in range(n):
    t, x, y = map(int, input().split())
    d.append([t, x, y])


def exe():
    for i in range(1, len(d)):
        dt = d[i][0] - d[i - 1][0]
        dist = abs(d[i][1] - d[i - 1][1]) + abs(d[i][2] - d[i - 1][2])
        if dt < dist or dist % 2 != dt % 2:
            print("No")
            exit(0)

    print("Yes")


if __name__ == '__main__':
    exe()
