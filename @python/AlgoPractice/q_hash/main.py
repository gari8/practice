from typing import List, Tuple, Optional


# def get_pair(numbers: List[int], target: int) -> tuple[int, int]:
#     for i in range(len(numbers) - 1):
#         for j in range(i, len(numbers)):
#             if (numbers[i] + numbers[j]) == target:
#                 return numbers[i], numbers[j]

def get_pair(numbers: List[int], target: int) -> tuple[int, int]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            print(val in cache)
            return val, num
        cache.add(num)


def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    half, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return
    cache = set()
    for num in numbers:
        val = half - num
        if val in cache:
            return val, num
        cache.add(num)


if __name__ == '__main__':
    nums = [11, 2, 5, 9, 10, 3]
    print(get_pair(nums, 12))
    print(get_pair_half_sum(nums))
