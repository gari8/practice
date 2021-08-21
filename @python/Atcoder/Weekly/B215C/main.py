import sys
input = sys.stdin.readline
n = int(input())

if __name__ == '__main__':
    if n >= 212:
        print(8)
    elif n >= 126:
        print(6)
    else:
        print(4)
