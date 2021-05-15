from typing import List


def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        pass


if __name__ == '__main__':
    import random

    nums = [5, 4, 1, 8, 7, 3, 2, 9]
    # nums = [random.randint(0, 1000) for _ in range(10)]
    print(merge_sort(nums))