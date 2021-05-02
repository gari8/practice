n, y = map(int, input().split())


def calc():
    for a in range(n+1):
        for b in range(n-a+1):
            c =n-a-b
            if c >= 0 and a * 10000 + b * 5000 + c * 1000 == y:
                print(a, b, c)
                exit(0)
    print("-1 -1 -1")


if __name__ == '__main__':
    calc()
