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
    int n, x;
    cin >> n;
    vi dp;
    for (int i = 0; i < n; i++) {
        cin >> x;
        int k = lower_bound(dp.begin(), dp.end(), x) - dp.begin();
        if (k == (int)dp.size()) {
            dp.push_back(x);
        } else {
            dp[k] = min(dp[k], x);
        }
    }
    cout << dp.size() << endl;
}
