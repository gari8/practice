import sys

input = sys.stdin.readline
K = int(input())


def bin_toi(s: str):
    return int(s.replace('0b', ''))


if __name__ == '__main__':
    print(bin_toi(bin(K)) * 2)
