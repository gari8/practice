import sys
input = sys.stdin.readline
a,b = map(int, input().split())

if __name__ == '__main__':
    if 0 < a and 0 < b:
        print("Alloy")
    elif a == 0 and 0 < b:
        print("Silver")
    else:
        print("Gold")