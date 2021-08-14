import sys
input = sys.stdin.readline
n = int(input())
al = list(map(int, input().split()))


if __name__ == '__main__':
    d = {}
    for i in range(n):
        d[al[i]] = i+1
    ms = max(al)
    al.remove(ms)
    mss = max(al)
    print(d[mss])
