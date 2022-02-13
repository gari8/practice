import sys

input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if __name__ == "__main__":
    ans = 0
    for i in range(N):
        ans += a[i] * b[i]

    if ans == 0:
        print("Yes")
    else:
        print("No")

