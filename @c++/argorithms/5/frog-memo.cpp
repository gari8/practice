//
// Created by HAGARI HAYATO on 2021/11/05.
//
#include <iostream>
#include <vector>

using namespace std;
const long long INF = 1LL << 60;

template<class T> void chmin(T& a, T b) {
    if (a > b) {
        a = b;
    }
}

long long rec(int i, vector<long long> h, vector<long long>& dp) {
    if (dp[i] < INF) return dp[i];

    if (i == 0) return 0;

    long long res = INF;

    chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]));

    if (i > 1) {
        chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]));
    }

    return dp[i] = res;
}

int main() {
    int N;
    cin >> N;
    vector<long long> h(N);
    for (int i = 0; i < N; ++i) cin >> h[i];
    vector<long long> dp(N, INF);

    cout << rec(N - 1, h, dp) << endl;

    return 0;
}