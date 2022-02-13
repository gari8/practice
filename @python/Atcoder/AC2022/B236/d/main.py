import sys

input = sys.stdin.readline
N = int(input())
A = [[]] * (2*N-1)
B = [[]] * (2*N-1)
for i in range(2*N-1):
    A[i] = list(map(int, input().split()))
    B[i] = [0] * len(A[i])


if __name__ == '__main__':
    print(A)
    print(B)