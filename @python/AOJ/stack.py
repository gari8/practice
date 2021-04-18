sl = list(map(str, input().split()))


def reverse_poland(lists):
    arr = []
    for i in lists:
        if i == '+':
            r = arr.pop(-2) + arr.pop(-1)
            arr.append(r)
        elif i == '-':
            r = arr.pop(-2) - arr.pop(-1)
            arr.append(r)
        elif i == '*':
            r = arr.pop(-2) * arr.pop(-1)
            arr.append(r)
        elif i == '/':
            r = arr.pop(-2) / arr.pop(-1)
            arr.append(r)
        else:
            arr.append(int(i))
    return arr


print(*reverse_poland(sl))
