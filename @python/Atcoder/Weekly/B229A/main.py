import sys

input = sys.stdin.readline
S1 = input()
S2 = input()
flag = True

if __name__ == '__main__':
    f = S1[0] != S1[1] and S1[0] != S1[1]
    f2 = S1[0] != S2[0] and S1[1] != S2[1]
    if f and f2:
        print("No")
    else:
        print("Yes")