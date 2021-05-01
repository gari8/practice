from typing import List


def comb_sort(numbers: List[int]) -> List[int]:
    return numbers


if __name__ == '__main__':
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    print(*comb_sort(nums))
