n, k = map(int, input().split())

if __name__ == '__main__':
    for i in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n)+"200")

    print(n)