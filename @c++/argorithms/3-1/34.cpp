//
// Created by HAGARI HAYATO on 2021/11/04.
//

#include <iostream>
#include <vector>
using namespace std;
const int INF = 20000000;

int main() {
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];
    int max_value = 0;
    int min_value = INF;

    for (int i = 0; i < N; ++i) {
        if (min_value > a[i]) {
            min_value = a[i];
        }

        if (max_value < a[i]) {
            max_value = a[i];
        }
    }

    cout << abs(max_value - min_value) << endl;
    return 0;
}