import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

dic = {}

if __name__ == '__main__':
    for i in range(len(A)):
        dic.setdefault(A[i], 0)
        dic[A[i]] += 1

    for k in dic:
        if dic[k] != 4:
            print(k)
            exit(0)
