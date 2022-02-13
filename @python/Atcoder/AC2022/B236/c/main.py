import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

if __name__ == '__main__':
    dic = {}
    for i in range(M):
        dic.setdefault(T[i], 0)

    for i in range(N):
        if S[i] in dic:
            print("Yes")
        else:
            print("No")
