n = int(input())
a_list = list(map(int, input().split()))

if __name__ == '__main__':
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a_list[i] != a_list[j]:
                cnt += 1
    print(cnt)