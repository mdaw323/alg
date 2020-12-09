#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int t, n, j;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> a = vector<int>(n);
        vector<int> l = vector<int>(n);
        vector<int> b;
        for (auto& ai : a) {
            cin >> ai;
        }
        for (auto& li : l) {
            cin >> li;
        }
        for (int i = 0; i < n; i++) {
            if (l[i] == 0) {
                b.push_back(a[i]);
            }
        }

        sort(b.rbegin(), b.rend());
        j = 0;
        for (int i = 0; i < n; i++) {
            if (l[i] == 1) {
                cout << a[i] << " ";
            } else {
                cout << b[j++] << " ";
            }
        }
        cout << endl;
    }
}
