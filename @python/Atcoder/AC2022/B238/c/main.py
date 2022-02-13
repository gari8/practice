import sys

input = sys.stdin.readline
N = int(input())
cons = 998244353


def loop_x(num: int) -> int:
    return int(0.5 * num * (num + 1))


if __name__ == '__main__':
    ans = 0
    if 0 <= N <= 9:
        ans += loop_x(N)
        print(N ,loop_x(N))
    elif N <= 99:
        ans += loop_x(N - 9)
        print(loop_x(N - 9))
    elif N <= 999:
        ans += loop_x(N - 99)
    elif N <= 9999:
        ans += loop_x(N - 999)
    elif N <= 99999:
        ans += loop_x(N - 9999)
    elif N <= 999999:
        ans += loop_x(N - 99999)
    elif N <= 9999999:
        ans += loop_x(N - 999999)
    elif N <= 99999999:
        ans += loop_x(N - 9999999)
    elif N <= 999999999:
        ans += loop_x(N - 99999999)
    elif N <= 9999999999:
        ans += loop_x(N - 999999999)
    elif N <= 99999999999:
        ans += loop_x(N - 9999999999)
    elif N <= 999999999999:
        ans += loop_x(N - 99999999999)
    elif N <= 9999999999999:
        ans += loop_x(N - 999999999999)
    elif N <= 99999999999999:
        ans += loop_x(N - 9999999999999)
    elif N <= 999999999999999:
        ans += loop_x(N - 99999999999999)
    elif N <= 9999999999999999:
        ans += loop_x(N - 999999999999999)
    elif N <= 99999999999999999:
        ans += loop_x(N - 9999999999999999)
    elif N <= 999999999999999999:
        ans += loop_x(N - 99999999999999999)
    else:
        ans += loop_x(N - 999999999999999999)

    print(ans)
