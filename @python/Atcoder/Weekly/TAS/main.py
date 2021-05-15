a1, a2, a3 = map(int, input().split())

if __name__ == '__main__':
    if (a3 - a2) == (a2 - a1) or (a3 - a1) == (a1 - a2) or (a1 - a2) == (a2 - a3) or (a2 - a1) == (a1 - a3) or (a1 - a3) == (a3 - a2) or (a2 - a3) == (a3 - a1):
        print("Yes")
    else:
        print("No")