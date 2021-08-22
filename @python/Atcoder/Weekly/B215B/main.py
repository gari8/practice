import sys
input = sys.stdin.readline
n = int(input())

if __name__ == '__main__':
    maxx = 0
    i = 0
    while maxx < n:
        if n >= pow(2, i):
            maxx = i
        else:
            break
        i += 1
    print(maxx)

