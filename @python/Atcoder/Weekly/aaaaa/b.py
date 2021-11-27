n = int(input())
sl = list(map(int, input().split()))

maxX = max(sl)


def predict(p):
    match = []
    for i in range(maxX // 4):
        ii = i + 1
        for j in range(maxX // 4):
            jj = j + 1
            ans = 4 * ii * jj + 3 * (ii + jj)
            if ans <= maxX:
                match.append(ans)
    return p in match


if __name__ == '__main__':
    cnt = 0
    for s in sl:
        if not predict(s):
            cnt += 1
    print(cnt)
