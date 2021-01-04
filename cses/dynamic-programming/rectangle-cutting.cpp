#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dp[501][501];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int a, b;
    cin >> a >> b;

    for (int i = 1; i <= a; i++) {
        for (int j = 1; j <= b; j++) {
            int m = 1e9;
            if (i == j) {
                m = 0;
            } else {
                for (int k = 1; k <= i/2; k++) {
                    m = min(m, 1 + dp[k][j] + dp[i - k][j]);
                }
                for (int l = 1; l <= j/2; l++) {
                    m = min(m, 1 + dp[i][l] + dp[i][j - l]);
                }
            }
            dp[i][j] = m;
        }
    }
    cout << dp[a][b] << endl;
}
