import sys

input = sys.stdin.readline
x, y = map(int, input().split("."))

if __name__ == '__main__':
    if 0 <= y <= 2:
        print(str(x)+"-")
    elif 7 <= y <= 9:
        print(str(x)+"+")
    else:
        print(str(x))
