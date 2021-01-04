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
    string a,b;
    int n,m;
    cin >> a >> b;
    n = (int)a.size();
    m = (int)b.size();
    vector<vector<int>> dp(n+1,vector<int>(m+1));
    for (int i = 1; i<=n; i++) {
        dp[i][0] = i;
    }
    for (int j = 1; j<=m; j++) {
        dp[0][j] = j;
    }

    int ins, upd, del;
    for (int i = 1; i<= n; i++) {
        for (int j = 1; j <= m ; j++) {
            ins = dp[i-1][j] + 1;
            upd = dp[i-1][j-1] + (a[i-1] == b[j-1] ? 0 : 1);
            del = dp[i][j-1] + 1;
            dp[i][j] = min(ins,min(upd,del));
        }
    }

    cout << dp[n][m] << endl;
}
