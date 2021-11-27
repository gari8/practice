n, k, a = map(int, input().split())

ll = []
j = a

for i in range(k):
    ll.append(j)
    if j == n:
        j = 0
    j += 1

if __name__ == '__main__':
    if n == 1:
        print(1)
        exit(0)
    print(ll[-1])