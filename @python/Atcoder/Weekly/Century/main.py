n = int(input())


if __name__ == '__main__':
    if n%100 == 0:
        print((n // 100))
    else:
        print((n//100)+1)