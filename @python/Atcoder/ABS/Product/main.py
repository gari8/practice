a, b = map(int, input().split())

if __name__ == '__main__':
    if (a*b) % 2 == 0:
        print("Even")
    else:
        print("Odd")