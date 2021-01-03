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
    int n;
    cin >> n;
    vi dp(1e6+1);
    dp[0] = 1;
    for (int i = 1; i<=n; i++) {
        for (int j = 1; j<=6; j++) {
            if (i-j>=0) {
                dp[i] = (dp[i] + dp[i-j]) % MOD;
            }
        }
    }
    cout << dp [n] << endl;
}
