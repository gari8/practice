n = int(input())

nums = list(map(int, input().split()))

cnt = 0

for i in range(n-1):
    minj = i
    for j in range(i, n):
        if nums[j] < nums[minj]:
            minj = j
    nums[i], nums[minj] = nums[minj], nums[i]
    if nums[i] != nums[minj]:
        cnt += 1

print(*nums)
print(cnt)