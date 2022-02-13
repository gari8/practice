import sys

input = sys.stdin.readline
N = int(input())
H = list(map(int, input().split()))


def move_right(l: list) -> int:
    cur = l[0]
    for i in range(1, N):
        if cur < l[i]:
            cur = l[i]
        else:
            return cur
    return cur


if __name__ == '__main__':
    print(move_right(H))
