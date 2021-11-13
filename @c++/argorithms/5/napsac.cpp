//
// Created by HAGARI HAYATO on 2021/11/05.
//
#include <iostream>
#include <vector>

using namespace std;
const long long INF = 1LL << 60;

template<class T>
void chmax(T &a, T b) {
    if (a < b) {
        a = b;
    }
}

int napsac(int i, int sum, int w, vector <vector<long long> > &dp, vector<long long> const weights,
           vector<long long> const values, const int n) {
    if (i == n) return sum;

    if (w - weights[i] >= 0) {
        chmax(dp[i + 1][w], dp[i][w]);
    }

    chmax(dp[i + 1][w], dp[i][w - weights[i]] + values[i]);

    return napsac(i - 1, sum, w, dp, weights, values, n);
}

int main() {
    int N, W;
    cin >> N >> W;
    vector<long long> weights(N), values(N);
    for (int i = 0; i < N; ++i) cin >> weights[i] >> values[i];
    vector <vector<long long> > dp(N + 1, vector<long long>(W + 1, -1));

    cout << napsac(N, 0, W, dp, weights, values, N) << endl;
    return 0;
}