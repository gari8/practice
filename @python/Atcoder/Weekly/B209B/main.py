n, x = map(int, input().split())
al = list(map(int, input().split()))

if __name__ == "__main__":
    cnt = 0
    for i in range(n):
        if i % 2 == 0:
            # odd
            x = x - al[i]
        else:
            # even
            x = x - al[i] + 1
    if x >= 0:
        print("Yes")
    else:
        print("No")
