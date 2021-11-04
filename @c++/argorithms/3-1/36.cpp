//
// Created by HAGARI HAYATO on 2021/11/04.
//

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int K, N;
    cin >> K >> N;
    int cnt = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            int z = K - i - j;
            if (z >= 0 && z <= K) {
                ++cnt;
            }
        }
    }

    cout << cnt << endl;
    return 0;
}