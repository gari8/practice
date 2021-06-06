from typing import List, Tuple

n = int(input())
nums = list(map(int, input().split()))


def selection_sort(numbers: List[int]) -> Tuple[List[int], int]:
    cnt = 0
    for i in range(len(numbers)):
        min_j = i
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[min_j]:
                min_j = j
        numbers[i], numbers[min_j] = numbers[min_j], numbers[i]
        if i != min_j:
            cnt += 1
    return numbers, cnt


if __name__ == '__main__':
    l, num = selection_sort(nums)
    print(*l)
    print(num)
