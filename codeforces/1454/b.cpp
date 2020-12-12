#include <bits/stdc++.h>

using namespace std;
using ll = int64_t;

int main() {
    int t, n;
    cin >> t;
    vector<int> s(200001);
    while (t--) {
        cin >> n;
        vector<int> a(n);
        for (auto &e : a) {
            cin >> e;
            s[e] = 0;
        }
        for (auto i : a) {
            s[i]++;
        }

        int ans = -2;
        for (int i = 0; i < n; i++) {
            if (s[a[i]] == 1 && (ans == -2 || a[i] < a[ans])) {
                ans = i;
            }
        }
        cout << ans + 1 << endl;
    }
}
