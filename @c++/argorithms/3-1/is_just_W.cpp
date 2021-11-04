//
// Created by HAGARI HAYATO on 2021/11/03.
//

#include <iostream>
#include <vector>
using namespace std;
const int INF = 20000000;

int main() {
    int N, W;
    cin >> N >> W;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    bool exists = false;
    for (int bit = 0; bit < (1 << N); ++bit) {
        int sum = 0;
        for (int i = 0; i < N; ++i) {
            if (bit & (1 << i)) {
                sum += a[i];
            }

        }

        if (sum == W) exists = true;
    }

    if (exists) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}