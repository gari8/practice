import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))


def get_max_space(l: list) -> int:
    if len(l) == 1:
        return max(360 - l[0], l[0] - 0)
    l.insert(0, 0)
    l.sort()
    max_space = -1
    for j in range(1, len(l)):
        max_space = max(abs(l[j] - l[j - 1]), max_space)
    max(abs(l[-1] - l[0]), max_space)
    return max_space


if __name__ == '__main__':
    z = [0] * N
    currentRadian = 0
    for i in range(N):
        if currentRadian == 0:
            z[i] = A[i]
            currentRadian = A[i]
        else:
            if currentRadian + A[i] > 360:
                z[i] = A[i] + currentRadian - 360
                currentRadian += A[i] - 360
            else:
                z[i] = A[i] + currentRadian
                currentRadian += A[i]

    print(get_max_space(z))
