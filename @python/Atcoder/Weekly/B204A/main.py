
x, y = map(int, input().split())

if __name__ == '__main__':
    te = [0, 1, 2]
    if x == y:
        print(x)
        exit(0)
    te.remove(x)
    te.remove(y)
    print(te[0])
