import math

S = input()

def check_str(code: str) -> int:
    cert_nums = 0
    un_cert_nums = 0
    no_nums = 0

    for i, s in enumerate(code):
        if s == 'o':
            cert_nums += 1
        elif s == '?':
            un_cert_nums += 1
        else:
            no_nums += 1

    if no_nums == 10 or cert_nums > 4:
        return 0
    elif cert_nums == 4:
        return math.factorial(4)
    else:
        left = 4 - cert_nums
        al = cert_nums + un_cert_nums
        return pow(al, left) + math.factorial(left) + cert_nums


if __name__ == '__main__':
    print(check_str(S))
