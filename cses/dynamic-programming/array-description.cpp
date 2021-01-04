#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

const ll MOD = 1e9 + 7;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    vi x(n);

    for (auto &i : x) {
        cin >> i;
    }
    vector<vector<ll>> dp(n, vector<ll>(m + 2));
    if (x[0] == 0) {
        for (int i = 1; i <= m; i++) {
            dp[0][i] = 1;
        }
    } else {
        dp[0][x[0]] = 1;
    }
    for (int j = 1; j < n; j++) {
        int z = x[j];
        if (z == 0) {
            for (int i = 1; i <= m; i++) {
                dp[j][i] = dp[j - 1][i - 1] + dp[j - 1][i] + dp[j - 1][i + 1];
                dp[j][i] %= MOD;

            }
        } else {
            dp[j][z] = dp[j - 1][z - 1] + dp[j - 1][z] + dp[j - 1][z + 1];
            dp[j][z] %= MOD;
        }
    }

    ll ans = 0;
    for (int     i = 1; i<=m; i++) {
        ans = (ans + dp[n-1][i]) % MOD;
    }
    cout << ans << endl;
}
