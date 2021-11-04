//
// Created by HAGARI HAYATO on 2021/11/04.
//

#include <iostream>
#include <vector>

using namespace std;
const int INF = 20000000;

int how_many_times(int N) {
    int exp = 0;
    while (N % 2 == 0) N /= 2, ++exp;
    return exp;
}

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    int min_value = INF;

    for (auto a: A) {
        min_value = min(min_value, how_many_times(a));
    }

    cout << min_value << endl;
    return 0;
}