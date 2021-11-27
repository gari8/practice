import sys

input = sys.stdin.readline
S, T, X = map(int, input().split())

if __name__ == '__main__':
    dist = 0
    if T < S:
        dist = T + (24 - S)
    else:
        dist = T - S

    ansDist = 0
    if X < S:
        ansDist = X + (24 - S)
    else:
        ansDist = X - S

    if dist <= ansDist:
        print("No")
    else:
        print("Yes")