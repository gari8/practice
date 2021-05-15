from typing import List


def partition(array: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(array: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(nums, low, high)
            _quick_sort(array, low, partition_index - 1)
            _quick_sort(array, partition_index + 1, high)

    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers


if __name__ == '__main__':
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    print(quick_sort(nums))
