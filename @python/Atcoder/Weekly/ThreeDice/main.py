a, b, c = map(int, input().split())


def calc(num: int) -> int:
    return 7 - num


if __name__ == '__main__':
    print(calc(a) + calc(b) + calc(c))
