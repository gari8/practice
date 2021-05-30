n, k = map(int, input().split())

if __name__ == '__main__':
    room_sum = 0
    for i in range(n):
        for j in range(k):
            room_num = int(str(i + 1) + '0' + str(j + 1))
            room_sum += room_num

    print(room_sum)