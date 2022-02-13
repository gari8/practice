import sys

input = sys.stdin.readline
S = input()
a, b = map(int, input().split())


if __name__ == '__main__':
    a -= 1
    b -= 1
    prefix = ''
    postfix = ''
    tmp = S[a]

    for i in range(len(S)):
        if i < a:
            prefix += S[i]
        if i > a:
            if i == b:
                postfix += tmp
            else:
                postfix += S[i]

    print(prefix+S[b]+postfix)


