import math

n = int(input())
nums = [int(input()) for _ in range(n)]


def is_prime(x):
    # 2は素数
    if x == 2:
        return True
    # 2未満、または偶数の場合は素数ではない
    if x < 2 or x % 2 == 0:
        return False
    # 3から√xまでの判定をすれば良い
    i = 3
    while i < math.ceil(math.sqrt(x)):
        if x % i == 0:
            return False
        i += 2
    return True


cnt = 0
for j in nums:
    if is_prime(j):
        cnt += 1

print(cnt)
