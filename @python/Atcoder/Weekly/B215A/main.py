import sys
input = sys.stdin.readline
s = input()
m = "Hello,World!"
if __name__ == '__main__':
    if s.strip() == m.strip():
        print("AC")
    else:
        print("WA")