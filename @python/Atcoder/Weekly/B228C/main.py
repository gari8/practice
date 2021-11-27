import sys

input = sys.stdin.readline
num = int(input())
cmd = []


def magic_a():
    global num
    cmd.append("A")
    num -= 1


def magic_b():
    global num
    cmd.append("B")
    num /= 2


if __name__ == '__main__':
    while num > 0:
        if num % 2 == 0:
            magic_b()
        else:
            magic_a()

    cmd.reverse()
    print(*cmd)
