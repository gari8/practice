import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

if __name__ == '__main__':
    cnt = 0
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(t[i])
            cnt = t[i]+s[i]
            continue
        if t[i] < cnt:
            ans.append(t[i])
            cnt = t[i]+s[i]
        else:
            ans.append(cnt)
            cnt = s[i]+cnt
    for i in range(n):
        print(ans[i])
