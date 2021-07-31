import sys
input = sys.stdin.readline
sl = [input().replace("\n", "") for _ in range(4)]
dic = {"H": 0, "2B": 0, "3B": 0, "HR": 0}

if __name__ == '__main__':
    for s in sl:
        dic[s] += 1
    for k in dic:
        if dic[k] == 0:
            print("No")
            exit(0)
    print("Yes")