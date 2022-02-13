import sys

input = sys.stdin.readline
N, X = map(int, input().split())
L = []
dp = []

for i in range(N):
    L.append(list(map(int, input().split()))[1:])
    dp.append([0] * len(L[i]))

for i in range(len(L[0])):
    if X % L[0][i] == 0:
        dp[0][i] = X // L[0][i]
    else:
        dp[0][i] = 0

for i in range(1, N):
    for j in range(len(L[i - 1])):
        for k in range(len(L[i])):
            if dp[i][j] % L[i][k] == 0:
                dp[i][j] = dp[i][j] // L[i][k]

if __name__ == '__main__':
    cnt = 0
    for i in dp[N-1]:
        if i != 0:
            cnt += 1
    print(cnt)