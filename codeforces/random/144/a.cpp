#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<int> h(n);

    int min_i = 0, max_i = 0;
    for (auto& s : h) {
        cin >> s;
    }

    for (int i = 1; i < n; i++) {
        if (h[i] > h[max_i]) {
            max_i = i;
        }
        if (h[i] <= h[min_i]) {
            min_i = i;
        }
    }

    int ans = max_i + ((n - 1) - min_i);
    if (max_i > min_i) {
        ans--;
    }
    cout << ans << endl;
}
