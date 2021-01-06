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
    vi x(n);
    for (auto &i : x) {
        cin >> i;
    }
    vi dp(n,1);
    int maxdp = 0;
    for (int i = 1; i<n; i++) {
        for (int j = 0; j<i; j++) {
            if (x[j] < x[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxdp= max(maxdp, dp[i]);
    }
    cout << maxdp << endl;
}
