//
// Created by HAGARI HAYATO on 2021/12/18.
//
#include <iostream>
#include <vector>

using namespace std;
const long long INF = 1LL << 60;

template<class T>
void chmax(T &a, T b) { if (a < b) a = b; }

template<class T>
void chmin(T &a, T b) { if (a > b) a = b; }

int main() {
    int N, W;
    cin >> N >> W;
    vector<long long> weight(N), value(N);
    for (int i = 0; i < N; ++i) cin >> weight[i] >> value[i];
    vector <vector<long long>> dp(N + 1, vector<long long>(W + 1, 0));

    for (int i = 0; i < N; ++i)
        for (int w = 0; w <= W; ++w) {
            if (w - weight[i] >= 0) {
                chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i]);
            }

            chmax(dp[i + 1][w], dp[i][w]);
        }

    cout << dp[N][W] << endl;
    return 0;
}