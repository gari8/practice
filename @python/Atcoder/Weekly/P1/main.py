a, b, c = map(int, input().split())


if __name__ == '__main__':
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    elif a == b == c:
        print(a)
    else:
        print(0)
