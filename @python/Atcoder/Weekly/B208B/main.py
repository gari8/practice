p = int(input())

if __name__ == '__main__':
    import math
    tmp = p
    ans = 0
    i = 10
    while tmp > 0 and i > 0:
        ni = math.factorial(i)
        if tmp - ni >= 0:
            ans += 1
            tmp -= ni
        else:
            i -= 1
    print(ans)