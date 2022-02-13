import sys

input = sys.stdin.readline
A, B = map(int, input().split())

if __name__ == '__main__':
    flag = False
    AS, BS = str(A)[::-1], str(B)[::-1]
    N = str(min(A, B))
    text = ""
    for i in range(len(N)):
        if int(AS[i]) + int(BS[i]) >= 10:
            flag = True

    if flag:
        print("Hard")
    else:
        print("Easy")
