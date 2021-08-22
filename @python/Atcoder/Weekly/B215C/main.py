import sys

input = sys.stdin.readline
s, k = map(str, input().split())

def perm(p):
    if len(p) == 1:
        return [p]
    else:
        s = []
        for i in range(len(p)):
            q = p[i]
            r = perm(p[:i]+p[i+1:])
            for t in r:
                s.append([q]+t)
        return s

if __name__ == '__main__':
    pp = perm(list(s))
    pp = list(map(lambda x: ''.join(x), pp))
    pp = list(set(pp))
    pp.sort()
    print(pp[int(k)-1])

