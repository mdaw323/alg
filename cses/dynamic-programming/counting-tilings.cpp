#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

const int MOD = 1e9 + 7;
int n, m;
int dp[1000][1024];

int add_mod(int a, int b) {
    ll c = (ll)a + b;
    if (c > MOD) {
        c -= MOD;
    }
    return (int)c;
}

void count_tiles(int i, int j, int cur_idx, int prev_idx) {
    if (i == n) {
        dp[j][cur_idx] = (j == 0 ? add_mod(dp[j][cur_idx], 1) : add_mod(dp[j][cur_idx], dp[j - 1][prev_idx]));
    } else {
        if (i < n - 1) count_tiles(i + 2, j, cur_idx, prev_idx);
        if (j < m - 1) count_tiles(i + 1, j, cur_idx | (1 << i), prev_idx);
        if (j > 0) count_tiles(i + 1, j, cur_idx, prev_idx | (1 << i));
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        count_tiles(0, i, 0, 0);
    }
    cout << dp[m - 1][0] << endl;
}
