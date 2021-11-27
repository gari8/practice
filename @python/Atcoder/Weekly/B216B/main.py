import sys
input = sys.stdin.readline
n = int(input())
nl = []
for _ in range(n):
    nn = input()
    nl.append(nn)

if __name__ == '__main__':
    nameMap = {}
    for ni in nl:
        if ni in nameMap:
            nameMap[ni] += 1
        else:
            nameMap[ni] = 1

    if len(nl) != len(set(nl)):
        print("Yes")
    else:
        print("No")