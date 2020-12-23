#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vi h(n);
    for (auto &h : h) {
        cin >> h;
    }
    vi dp(n + 1, 1e9);
    dp[0] = 0;

    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= k; j++) {
            if (i - j >= 0) {
                dp[i] = min(dp[i], abs(h[i] - h[i - j]) + dp[i - j]);
            }
        }
    }
    cout << dp[n - 1] << endl;
}
