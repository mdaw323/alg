#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main () {
    int n,r;
    vector<int> N;
    unordered_map<int, int> left_side;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> r;
        N.push_back(r);
    }

    for (int d : N) {
        if (d == 0) continue;
        for (int e : N) {
            for (int f : N) {
                int key = d * (f + e);
                auto search = left_side.find(key);
                if (search != left_side.end()) {
                    search->second +=1;
                } else {
                    left_side[key] = 1;
                }
            }
        }
    }

    unsigned long res = 0;
    for (int a : N) {
        for (int b : N) {
            for (int c : N)  {
                auto search = left_side.find(a*b+c);
                if (search != left_side.end()) {
                    res += search->second;
                }
            }
        }
    }

    cout << res;
    return 0;
}
