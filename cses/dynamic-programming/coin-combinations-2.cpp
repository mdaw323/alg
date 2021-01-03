#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, x;
    cin >> n >> x;
    vi c(n);
    for (auto &i : c) {
        cin >> i;
    }
    vi dp(x + 1);
    dp[0] = 1;
    for (int j = 0; j < n; j++) {
        for (int i = 1; i <= x; i++) {
            if (i - c[j] >= 0) {
                dp[i] = (dp[i] + dp[i - c[j]]) % MOD;
            }
        }
    }

    cout << dp[x] << endl;
}
