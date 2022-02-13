import sys

input = sys.stdin.readline
N, K = map(int, input().split())
P = list(map(int, input().split()))


def self_index(col, k):
    col.sort(reverse=True)
    return col[k - 1]


if __name__ == '__main__':
    for i in range(K, N + 1):
        print(self_index(P[:i], K))
