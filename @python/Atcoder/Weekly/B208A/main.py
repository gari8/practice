a, b = map(int, input().split())
lim = a*6
ans = lim >= b >= a
if __name__ == '__main__':
    if b == 0 or a == 0:
        print("No")
    if ans:
        print("Yes")
    else:
        print("No")