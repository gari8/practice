import sys

input = sys.stdin.readline
N = int(input())

if __name__ == "__main__":
    dic = {}
    col = []
    for i in range(N):
        s, t = map(str, input().split())
        col.append(int(t))
        dic.setdefault(int(t), s)

    col.sort(reverse=True)
    print(dic[col[1]])
