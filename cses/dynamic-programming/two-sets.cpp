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
    cin >> n;
    x = n * (n + 1) / 2;
    if (x % 2 == 1) {
        cout << 0 << endl;
        return 0;
    }
    x = x / 2;
    vi dp(x + 1);
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = x; j - i >= 0; j--) {

            if (j == x) {
                dp[j] = dp[j - i];
            } else {
                dp[j] = (dp[j] + dp[j - i]) % MOD;
            }
        }
    }
    cout << dp[x] << endl;
}
