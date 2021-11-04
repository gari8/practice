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

    int min_value = INF;
    int next_min_value = INF;
    for (int i = 0; i < N; ++i) {
        if (min_value > a[i]) {
            next_min_value = min_value;
            min_value = a[i];
        } else if (next_min_value > a[i]) {
            next_min_value = a[i];
        }
    }

    cout << min_value << ":" << next_min_value << endl;
    return 0;
}