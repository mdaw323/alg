#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vi x(n);
    for (auto &i : x) {
        cin >> i;
    }
    vector<vector<ll>> dp(n, vector<ll>(n));
    for (int i = 0; i < n; i++) {
        dp[i][i] = x[i];
        if (i > 0) {
            dp[i - 1][i] = max(x[i - 1], x[i]);
        }
    }
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i + 2; j < n; j++) {
            ll l, r, p;
            l = i + 1;
            r = j;
            p = min(dp[l + 1][r], dp[l][r - 1]);
            dp[i][j] = p + x[i];

            l = i;
            r = j - 1;
            p = min(dp[l + 1][r], dp[l][r - 1]);
            dp[i][j] = max(dp[i][j], p + x[j]);
        }
    }
    cout << dp[0][n - 1] << endl;
}
