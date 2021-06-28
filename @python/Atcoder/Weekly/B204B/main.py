n = int(input())
a_list = list(map(int, input().split()))

if __name__ == '__main__':
    ans = 0
    for tree in a_list:
        if tree > 10:
            ans += tree - 10
    print(ans)
