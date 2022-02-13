import sys

input = sys.stdin.readline
N, M = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(M)]
A = [list(map(int, input().split())) for _ in range(M)]


def check_same(a, b):
    a.sort()
    b.sort()
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return False
    return True


if __name__ == '__main__':
    lt, la = [], []

    for i in range(N+1):
        lt.append(0)
        la.append(0)

    for i in range(M):
        [a, b] = T[i]
        lt[a] += 1
        lt[b] += 1

        [c, d] = A[i]
        la[c] += 1
        la[d] += 1

    if check_same(lt, la):
        print("Yes")
    else:
        print("No")
