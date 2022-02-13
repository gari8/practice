import sys

input = sys.stdin.readline
L, R = map(int, input().split())
S = input()

if __name__ == '__main__':
    left = S[:L-1]
    right = S[R:]
    center = S[L-1:R]
    print(left+center[::-1]+right)