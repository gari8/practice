import math

n = int(input())
a_list = list(map(int, input().split()))

if __name__ == '__main__':
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans = abs(a_list[i] - a_list[i+1])
            if ans % 200 == 0:
                cnt += 1

    print(cnt)