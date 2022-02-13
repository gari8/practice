import sys

input = sys.stdin.readline
abc = input()


def rotate(num: str) -> int:
    return int(num) + int(num[1] + num[2] + num[0]) + int(num[2] + num[0] + num[1])


if __name__ == '__main__':
    print(rotate(abc))
