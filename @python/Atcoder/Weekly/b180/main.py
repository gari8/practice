S = input()


def create_string(st: str) -> str:
    new_st = ''
    for s in st:
        if s == '0':
            new_st += s
        elif s == '1':
            new_st += s
        elif s == '6':
            new_st += '9'
        elif s == '8':
            new_st += s
        elif s == '9':
            new_st += '6'
    return new_st[::-1]


if __name__ == '__main__':
    print(create_string(S))
