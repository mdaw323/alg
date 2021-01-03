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
    string s;
    int n;
    cin >> n;
    vi dp(n + 1);
    dp[1] = 1;
    for (int i = 1; i <= n; i++) {
        cin >> s;
        for (int y = 1; y <= n; y++) {
            if (s[y - 1] == '*') {
                dp[y] = 0;
            } else {
                dp[y] = (dp[y - 1] + dp[y]);
                if (dp[y] > MOD) {
                    dp[y] -= MOD;
                }
            }
        }
    }
    cout << dp[n] << endl;
}
