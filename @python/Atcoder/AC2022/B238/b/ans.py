import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    cut = [0, 360]
    cumulative_sum = 0
    for i in range(N):
        if cumulative_sum + A[i] > 360:
            cumulative_sum = (cumulative_sum + A[i]) % 360
            cut.append(cumulative_sum)
        else:
            cumulative_sum += A[i]
            cut.append(cumulative_sum)
    cut.sort()
    max_space = 0
    for index in range(len(cut)):
        max_space = max(cut[index] - cut[index - 1], max_space)
    print(max_space)
