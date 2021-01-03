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
    int n;
    cin >> n;
    vi dp(n + 1, 1e9);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        int k = i;
        while (k > 0)  {
            int d = k % 10;
            dp[i] = min(dp[i], dp[i - d] + 1);
            k /=10;
        }
    }
    cout << dp[n] << endl;

}
