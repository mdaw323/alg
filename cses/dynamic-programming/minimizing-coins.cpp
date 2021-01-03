#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, x;
    cin >> n >> x;
    vi c(n);
    for (auto &i : c) {
        cin >> i;
    }
    vi dp(x + 1, INF);
    dp[0] = 0;
    for (int i = 1; i <= x; i++) {
        for (int j = 0; j < n; j++) {
            if (i - c[j] >= 0) {
                dp[i] = min(dp[i], dp[i - c[j]] + 1);
            }
        }
    }
    cout << (dp[x] == INF ? -1 : dp[x]) << endl;
}
