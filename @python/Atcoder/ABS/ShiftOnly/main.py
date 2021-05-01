from typing import List


def rec_list(array: List[int], cnt: int):
    new_list = []
    flag = False
    for i in array:
        if i % 2 == 0:
            new_list.append(int(i / 2))
        else:
            flag = True

    if flag:
        print(cnt)
        exit(0)
    else:
        rec_list(new_list, cnt + 1)


if __name__ == "__main__":
    n = int(input())
    a_list = list(map(int, input().split()))

    rec_list(a_list, 0)
