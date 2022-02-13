import sys

input = sys.stdin.readline
N = int(input())


if __name__ == '__main__':
    if not(N == 2 or N == 3 or N == 4):
        print("Yes")
    else:
        print("No")