//
// Created by HAGARI HAYATO on 2021/12/18.
//

#include <iostream>
#include <vector>

using namespace std;
const long long INF = 1LL << 60;

template<class T> void chmax(T& a, T b) { if (a < b) a = b; }
template<class T> void chmin(T& a, T b) { if (a > b) a = b; }

int main() {
    int N, W;
    cin >> N >> W;
    vector<long long> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    vector<vector<bool> > dp(N + 1, vector<bool>(W+1, false));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j <= W; ++j) {
            if (dp[i][j]) dp[i+1][j] = true;

            if (j >= a[i] && dp[i][j - a[i]]) dp[i+1][j] = true;
        }
    }

    if (dp[N][W]) cout << "Yes" << endl;
    else cout << "No" << endl;

    return 0;
}