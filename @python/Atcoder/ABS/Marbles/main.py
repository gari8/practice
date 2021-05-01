stripe = input()

cnt = 0

for s in stripe:
    if int(s) == 1:
        cnt += 1

if __name__ == '__main__':
    print(cnt)
