import sys

input = sys.stdin.readline

a, N = map(int, input().split())


def rolling(s: str, n: int) -> str:
    return s[n:len(s)] + s[:n]


def rotate_int(x: int) -> int:
    if x >= 10 and x % 10 != 0:
        return int(rolling(str(x), len(str(x)) - 1))
    else:
        return -1


if __name__ == '__main__':
    X = 1
    cnt = 0

    while X < N:
        print(cnt, X)
        if N % a == 0:
            X *= a
        else:
            if rotate_int(X) == -1:
                break
            else:
                X = rotate_int(X)

    print("last: ", cnt, X)

    if X == N:
        print(cnt)
    else:
        print(-1)