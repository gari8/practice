n, a, b = map(int, input().split())


def some_sums():
    ans = 0
    for i in range(1, n + 1):
        sms = 0
        for s in str(i):
            sms += int(s)
        if a <= sms <= b:
            ans += i

    return ans


if __name__ == '__main__':
    print(some_sums())
