import sys
input = sys.stdin.readline
n, k = map(int, input().split())
cl = list(map(int, input().split()))

if __name__ == '__main__':
    max_size = -1
    for i in range(0, n - k + 1):
        ll = set(cl[i:i+k])
        if max_size <= len(ll):
            max_size = len(ll)
    print(max_size)