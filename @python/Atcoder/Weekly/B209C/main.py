n = int(input())
cl = list(map(int, input().split()))

if __name__ == "__main__":
    mod = 10**9+7
    ans = 1
    for i in range(n):
        c = cl[i] - i
        ans = ((ans % mod) * (c % mod)) % mod
    print(ans)