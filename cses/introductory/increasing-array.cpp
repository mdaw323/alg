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
    ll x, p, ans = 0;
    cin >> n;
    cin >> p;
    for (int i = 1; i < n; i++) {
        cin >> x;
        if (x < p) {
            ans += p - x;
        }
        p = max(x, p);
    }
    cout << ans << endl;
}
