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
    int n;
    cin >> n;
    vi heights(n);
    for (auto &h : heights) {
        cin >> h;
    }
    vi dp(n + 1, 1e9);
    dp[0] = 0;
    dp[1] = abs(heights[1] - heights[0]);

    for (int i = 2; i < n; i++) {
        dp[i] = min(
            abs(heights[i] - heights[i - 1]) + dp[i - 1],
            abs(heights[i] - heights[i - 2]) + dp[i - 2]);
    }
    cout << dp[n - 1] << endl;
}
