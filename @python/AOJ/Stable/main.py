from typing import List, Tuple

n = int(input())
nums = list(map(str, input().split()))

def selection_sort(numbers: List[str]) -> None:
    cnt = 0
    for i in range(len(numbers)):
        min_j = i
        for j in range(i, len(numbers)):
            if numbers[j][1] < numbers[min_j][1]:
                min_j = j
        numbers[i], numbers[min_j] = numbers[min_j], numbers[i]
        if i != min_j:
            cnt += 1

def bubble_sort(numbers: List[str]) -> None:
    flag = 1
    cnt = 0
    i = 0
    while flag:
        flag = 0
        for j in range(len(numbers) - 1, i, -1):
            if numbers[j][1] < numbers[j - 1][1]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
                flag = 1
                cnt += 1
        i += 1



def stable_sort(numbers: List[str]) -> None:
    A_bub = numbers[:]
    bubble_sort(A_bub)
    print(*A_bub)
    print("Stable")

    selection_sort(numbers)
    print(*numbers)
    print("Stable" if numbers == A_bub else "Not stable")


if __name__ == '__main__':
    stable_sort(nums)
