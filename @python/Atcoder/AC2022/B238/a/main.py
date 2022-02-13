import sys

input = sys.stdin.readline
N = int(input())


if __name__ == '__main__':
    if N > 4 or N <= 1:
        print("Yes")
    else:
        print("No")


