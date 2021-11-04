//
// Created by HAGARI HAYATO on 2021/11/03.
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, v;
    cin >> N >> v;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    bool exists = false;
    for (int i = 0; i < N; ++i) {
        if (a[i] == v) {
            exists = true;
        }
    }

    if (exists) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}
