from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    a, b = map(str, input().split())
    d.append([a, int(b)])

if __name__ == '__main__':
    maxI = 0
    for i in range(len(d)):
        if d[maxI][1] < d[i][1]:
            maxI = i
    del d[maxI]
    maxI = 0
    for i in range(len(d)):
        if d[maxI][1] < d[i][1]:
            maxI = i
    print(d[maxI][0])
