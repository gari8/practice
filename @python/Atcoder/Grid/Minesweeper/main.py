H, W = map(int, input().split())
S_LIST = [input() for _ in range(H)]


def exe():
    for i in range(H - 1):
        for j in range(W - 1):
            if i == 0 or j == 0:
                print("current", S_LIST[i][j], "right", S_LIST[i][j + 1], "bottom", S_LIST[i + 1][j], "right_bottom",
                      S_LIST[i + 1][j + 1])
            else:
                print("current", S_LIST[i][j], "top", S_LIST[i][j - 1], "right", S_LIST[i][j + 1], "bottom",
                      S_LIST[i + 1][j], "left", S_LIST[i][j - 1], "top_right", S_LIST[i - 1][j + 1], "right_bottom",
                      S_LIST[i + 1][j + 1], "left_bottom")


if __name__ == '__main__':
    exe()
