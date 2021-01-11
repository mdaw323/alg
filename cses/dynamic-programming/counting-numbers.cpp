#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dp[19];

ll count(ll x) {
    vector<ll> a;
    while (x > 0) {
        a.push_back(x % 10);
        x /= 10;
    }

    int n = (int)a.size();
    ll s = 0;
    for (int i = n - 1; i >= 0; --i) {
        s += dp[i];
    }
    ll last_digit = 0;
    for (int i = n - 1; i >= 0; --i) {
        for (int j = 0; j < a[i]; ++j) {
            if (j != last_digit) {
                s += dp[i];
            }
        }
        if (a[i] == last_digit) break;
        last_digit = a[i];
    }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll a, b;
    cin >> a >> b;
    dp[0] = 1;

    for (int i = 1; i < 19; i++) {
        for (int j = 0; j < 9; j++) {
            dp[i] += dp[i - 1];
        }
    }
    cout << count(b + 1) - count(a) << endl;
}
