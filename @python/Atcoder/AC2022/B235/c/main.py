import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
XK = []
for i in range(Q):
    XK.append(list(map(int, input().split())))

mp = {}


def judge(obj, n, c) -> int:
    if n in obj and len(obj[n]) >= c:
        return obj[n][c-1] + 1
    else:
        return -1


if __name__ == '__main__':
    for i in range(N):
        mp.setdefault(A[i], [])
        mp[A[i]].append(i)

    for i in range(Q):
        [num, cnt] = XK[i]
        print(judge(mp, num, cnt))
