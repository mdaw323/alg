#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

//Knapsack
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n, W, max_value = 0;
    cin >> n >> W;
    vl w(n), v(n);

    for (ll i = 0; i < n; i++) {
        cin >> w[i] >> v[i];
        max_value += v[i];
    }
    vl dp(max_value + 1, 1e18);

    dp[0] = 0;
    for (ll i = 0; i < n; i++) {
        for (ll j = max_value; j - v[i] >= 0; --j) {
            dp[j] = min(dp[j], dp[j - v[i]] + w[i]);
        }
    }
    ll ans = 0;
    for (ll j = 1; j <= max_value; j++) {
        if (dp[j] <= W) {
            ans = j;
        }
    }
    cout << ans << endl;
}
