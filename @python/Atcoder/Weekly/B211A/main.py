import sys
input = sys.stdin.readline
a,b = map(int, input().split())

if __name__ == '__main__':
    s = a + (2*b)
    print(s / 3)