N, M = map(int, input().split())
A, B = [], []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

if __name__ == '__main__':
    conv = []
    bbb = set(B)
    aaa = set(A)
    if M == 0:
        print(N)
        exit(0)
    for aa in aaa:
        for bb in bbb:
            if not (str(aa)+str(bb) in conv) and not(aa == bb):
                conv.append(str(aa)+str(bb))
    print(N + len(conv))
