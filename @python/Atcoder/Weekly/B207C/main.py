from typing import List

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]


def exp(ar: List[int]):
    if ar[0] == 1:
        s, e = ar[1:]
        return list(range(s, e + 1, 1))
    elif ar[0] == 2:
        s, e = ar[1:]
        return list(range(s, e, 1))
    elif ar[0] == 3:
        s, e = ar[1:]
        return list(range(s + 1, e + 1, 1))
    else:
        s, e = ar[1:]
        return list(range(s + 1, e, 1))


if __name__ == '__main__':
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            il = exp(l[i])
            jl = exp(l[j])
            il.extend(jl)
            ans += len(il) - len(set(il))
    print(ans)
