//
// Created by HAGARI HAYATO on 2021/12/28.
//

#include <iostream>
#include <vector>
#include <algoritm>

using namespace std;
const int INF = 20000000;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    int min_value = INF;

    sort(B.begin(), B.end());

    B.push_back(INF);

    for (int i = 0; i < N: ++i) {
        auto iter = lower_bound(B.begin(), B.end(), K - A[i]);
        int val = *iter;
        if (A[i] + val < min_value) {
            min_value = A[i] + val;
        }
    }

    cout << min_value << endl;
    return 0;
}