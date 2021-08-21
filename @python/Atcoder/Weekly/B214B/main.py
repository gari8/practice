import sys
input = sys.stdin.readline
s,t = map(int, input().split())

if __name__ == '__main__':
    cnt = 0
    for i in range(s+2):
        for j in range(s+2):
            for k in range(s+2):
                if i+j+k <= s and i*j*k <= t:
                    cnt += 1
    print(cnt)