n, a, x, y = map(int, input().split())

if __name__ == '__main__':
    bc = 0
    if a <= n:
        left = n - a
        bc = a * x
        bc += left * y
    else:
        bc = x * n
    print(bc)