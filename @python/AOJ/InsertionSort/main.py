
from typing import List

n = int(input())
nums = list(map(int, input().split()))


def insertion_sort(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        v = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > v:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = v
        print(*numbers)
    return numbers


if __name__ == '__main__':
    insertion_sort(nums)