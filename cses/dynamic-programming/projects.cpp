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
    int n, x, y, z;
    cin >> n;
    vector<tuple<int, int, int>> p(n + 1);

    p[0] = {0, 0, 0};
    for (int i = 1; i <= n; i++) {
        cin >> x >> y >> z;
        p[i] = {y, x, z};
    }

    sort(p.begin(), p.end());

    vl dp(n+1);
    for (int i = 1; i<=n; i++) {
        tie(y, x, z) = p[i];
        auto u = upper_bound(p.begin(), p.begin() + i, make_tuple(x,0,0));
        int j = distance(p.begin(), u-1);
        dp[i] = max(dp[i-1], dp[j] + z);
    }
    cout << dp[n] << endl;
}
