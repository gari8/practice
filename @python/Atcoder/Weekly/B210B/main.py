n = int(input())
s = input()

if __name__ == '__main__':
    t = "Takahashi"
    a = "Aoki"
    for i in range(n):
        if s[i] == "1":
            if i % 2 == 0:
                print(t)
            else:
                print(a)
            exit(0)