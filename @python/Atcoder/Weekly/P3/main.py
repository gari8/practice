n, k = map(int, input().split())
ck = k
kv = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a in kv:
        kv[a] += b
    else:
        kv[a] = b

if __name__ == '__main__':
    ind = 0
    pre = 0
    for key in kv:
        ind = key
        ck -= key - pre
        if key in kv:
            ck += kv[key]
        if ck <= 0:
            break
        pre = key

    print(ck + ind)
