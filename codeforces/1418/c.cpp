#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) {
        int n, r1, r2;
        cin >> n;
        vector<int> hard(n + 2, 0);
        vector<vector<int>> dp(n + 2, vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> hard[i];
        }
        dp[n][0] = dp[n][1] = dp[n + 1][1] = dp[n + 1][0] = 0;
        for (int i = n - 1; i >= 0; i--) {
            for (int k = 0; k < 2; k++) {
                r1 = hard[i] * k;
                r2 = hard[i + 1] * k;
                dp[i][k] = min(r1 + dp[i + 1][k ^ 1], r1 + r2 + dp[i + 2][k ^ 1]);
            }
        }
        cout << dp[0][1] << endl;
    }
}
