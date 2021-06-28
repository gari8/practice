import math

a, b, c, d = map(int, input().split())

if __name__ == '__main__':

    if b > (c * d):
        print(-1)
        exit(0)
    if c == 0 or d == 0:
        print(-1)
        exit(0)
    if a != 0:
        at = (c * d - b)
        if at == 0:
            print(-1)
            exit(0)
        tmp = a / at
        print(math.ceil(tmp))
        exit(0)
    print(-1)
