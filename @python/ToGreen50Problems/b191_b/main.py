import sys

input = sys.stdin.readline
N, X = map(int, input().split())
a = list(map(int, input().split()))

if __name__ == "__main__":
    a_dash = []

    for i in range(N):
        if a[i] != X:
            a_dash.append(a[i])

    print(*a_dash)
