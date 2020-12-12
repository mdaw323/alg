#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, n;
    vector<int> s(200001, 0);
    cin >> t;

    while (t--) {
        cin >> n;
        vector<int> a(n);
        for (auto &i : a) {
            cin >> i;
            s[i] = 1;
        }
        int last = a[0];
        for (int i = 1; i < n; i++) {
            if (last != a[i]) {
                s[a[i]]++;
            }
            last = a[i];
        }
        s[last]--;

        int min_i = 0;
        for (int i = 1; i < n; i++) {
            if (s[a[min_i]] > s[a[i]]) {
                min_i = i;
            }
        }

        cout << s[a[min_i]] << endl;
    }
}
