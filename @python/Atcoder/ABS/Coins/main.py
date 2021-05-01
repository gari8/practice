# 500 coin
a = int(input())
# 100 coin
b = int(input())
# 50 coin
c = int(input())
x = int(input())

if __name__ == "__main__":
    cnt = 0
    for ac in range(0, a + 1):
        for bc in range(0, b + 1):
            for cc in range(0, c + 1):
                if ac * 500 + bc * 100 + cc * 50 == x:
                    cnt += 1

    print(cnt)
