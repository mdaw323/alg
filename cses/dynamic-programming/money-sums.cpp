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
    int n, N, x;
    cin >> n;

    N = n * 1000;
    vector<bool> dp(N + 1);
    dp[0] = true;
    for (int j = 0; j < n; j++) {
        cin >> x;
        for (int i = N; i >= x; i--) {
            if (dp[i - x]) {
                dp[i] = true;
            }
        }
    }
    int ans = 0;
    for (int i = 1; i<= N; i++) {
        if (dp[i]) {
            ans += 1;
        }
    }
    cout << ans << endl;
    for (int i = 1; i<= N; i++) {
        if (dp[i]) {
            cout << i << " ";
        }
    }
    cout << endl;
}
