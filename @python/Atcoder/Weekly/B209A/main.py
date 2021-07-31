a, b = map(int, input().split())


if __name__ == "__main__":
    if a > b:
        print(0)
    else:
        print(b-a+1)