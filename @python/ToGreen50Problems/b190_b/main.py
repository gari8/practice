import sys

input = sys.stdin.readline
N, S, D = map(int, input().split())

if __name__ == "__main__":
    is_attacked = False
    for i in range(N):
        x, y = map(int, input().split())
        if x < S and y > D:
            is_attacked = True

    if is_attacked:
        print("Yes")
    else:
        print("No")