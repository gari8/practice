n = int(input())

if __name__ == '__main__':
    import math
    con = math.floor(n * 1.08)
    if con < 206:
        print("Yay!")
    elif con == 206:
        print("so-so")
    else:
        print(":(")
