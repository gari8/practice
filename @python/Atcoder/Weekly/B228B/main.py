import sys

input = sys.stdin.readline

n, x = map(int, input().split())
a_list = list(map(int, input().split()))

mpp = {}

if __name__ == '__main__':
    flag = True
    i = x
    while flag:
        if not a_list[i - 1] in mpp:
            mpp[i] = True
            i = a_list[i - 1]
        else:
            flag = not flag
    print(len(mpp) + 1)
