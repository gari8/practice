#include <iostream>
#include <vector>
#include <random>

using namespace std;

vector<int> generate_array(int length, int low = 0, int high = 100) {
    vector<int> array;
    for (int i = 0; i < length; ++i) {
        int distance = high - low;
        int random = rand % distance + low;
        array.push_back(random);
    }
    return array;
}

void quick_sort(vector<int>) {
}

int main() {
    vector<int> array = generate_array(10, 0, 10000);
    for (int i = 0; i < array.size(); ++i) {
        cout << array[i];
    }
    return 0;
}