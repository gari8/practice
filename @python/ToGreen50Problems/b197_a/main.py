import sys

input = sys.stdin.readline
s = input()

if __name__ == "__main__":
    ans = s[1:].replace("\n", "") + s[0]
    print(ans)
