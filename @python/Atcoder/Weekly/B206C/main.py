n = int(input())
a_list = list(map(int, input().split()))

if __name__ == '__main__':
    ans = 0
    cnt = {}
    for j in range(n):
        cnt.setdefault(a_list[j], 0)
        ans += j - cnt[a_list[j]]
        cnt[a_list[j]] += 1
    print(ans)