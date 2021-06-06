from typing import List

formula = list(map(str, input().split()))


def reverse_poland(S_LIST: List[str]) -> int:
    stack = []
    for i in range(len(S_LIST)):
        if S_LIST[i] == '+':
            last = stack.pop()
            pre_last = stack.pop()
            stack.append(last + pre_last)
        elif S_LIST[i] == '-':
            last = stack.pop()
            pre_last = stack.pop()
            stack.append(pre_last - last)
        elif S_LIST[i] == '*':
            last = stack.pop()
            pre_last = stack.pop()
            stack.append(pre_last * last)
        else:
            stack.append(int(S_LIST[i]))
    return stack[0]


if __name__ == '__main__':
    print(reverse_poland(formula))
