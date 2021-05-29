from typing import List

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
c_list = [c_list[i] - 1 for i in range(n)]


def search_rec(list_a: List[int], list_b: List[int], list_c: List[int], length: int) -> int:
    def _search_rec(i, j, cnt):
        if i >= length:
            return cnt
        if j >= length:
            i += 1
            j = 0
            return _search_rec(i, j, cnt)
        if list_a[i] == list_b[list_c[j]]:
            cnt += 1
        return _search_rec(i, j + 1, cnt)

    return _search_rec(0, 0, 0)


if __name__ == '__main__':
    print(search_rec(a_list, b_list, c_list, n))
