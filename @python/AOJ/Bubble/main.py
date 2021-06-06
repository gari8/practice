from typing import List, Tuple

n = int(input())
nums = list(map(int, input().split()))


def bubble_sort(numbers: List[int]) -> Tuple[List[int], int]:
    flag = 1
    cnt = 0
    i = 0
    while flag:
        flag = 0
        for j in range(len(numbers) - 1, i, -1):
            if numbers[j] < numbers[j - 1]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                flag = 1
                cnt += 1
        i += 1
    return numbers, cnt


if __name__ == '__main__':
    l, num = bubble_sort(nums)
    print(*l)
    print(num)
