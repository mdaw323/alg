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
    vi a(n), b(n), c(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> b[i] >> c[i];
    }
    vi dp_a(n, 0);
    vi dp_b(n, 0);
    vi dp_c(n, 0);

    dp_a[0] = a[0];
    dp_b[0] = b[0];
    dp_c[0] = c[0];

    for (int i = 1; i < n; i++) {
        dp_a[i] = a[i] + max(dp_b[i - 1], dp_c[i - 1]);
        dp_b[i] = b[i] + max(dp_a[i - 1], dp_c[i - 1]);
        dp_c[i] = c[i] + max(dp_b[i - 1], dp_a[i - 1]);
    }
    cout << max(max(dp_a[n - 1], dp_b[n - 1]), dp_c[n - 1]) << endl;
}
