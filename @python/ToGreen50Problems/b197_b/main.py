import sys

input = sys.stdin.readline
H, W, Y, X = map(int, input().split())
S = [input() for _ in range(H)]

if __name__ == "__main__":
    height = 0
    height_ok = False
    width = 0
    width_ok = False
    for i in range(H):
        if S[i][X - 1] == "#":
            if height_ok:
                break
            else:
                height = 0
        else:
            height += 1
            if i == Y - 1:
                height_ok = True

    for i in range(W):
        if S[Y - 1][i] == "#":
            if width_ok:
                break
            else:
                width = 0
        else:
            width += 1
            if i == X - 1:
                width_ok = True

    print(height + width - 1)

