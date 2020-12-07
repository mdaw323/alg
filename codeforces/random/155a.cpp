#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int n,x, min_perf, max_perf, amazing = 0;
    cin >> n;
    cin >> x;
    min_perf = max_perf = x;

    for (int i = 1; i <n; i++) {
        cin >> x;
        if (x < min_perf) {
            amazing++;
            min_perf = x;
        }
        if (x > max_perf) {
            amazing ++;
            max_perf = x;
        }
    }
    cout << amazing << endl;
}
