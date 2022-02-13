import sys
import string

input = sys.stdin.readline
S = input().rstrip('\n')
T = input().rstrip('\n')


if __name__ == '__main__':
    alphabet = list(string.ascii_lowercase)
    for i in range(len(alphabet)):
        s = ''
        for j in range(len(S)):
            idx = alphabet.index(S[j]) + i

            if idx >= len(alphabet):
                idx -= len(alphabet)
            if idx == alphabet.index(T[j]):
                s += alphabet[idx]
        if s == T:
            print("Yes")
            exit(0)

    print("No")
