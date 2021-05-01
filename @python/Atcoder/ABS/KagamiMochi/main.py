n = int(input())
ds = [int(input()) for _ in range(n)]

ds.sort(reverse=True)

cnt = 1

current = ds[0]

for d in ds:
    if current > d:
        cnt += 1
        current = d

if __name__ == '__main__':
    print(cnt)
