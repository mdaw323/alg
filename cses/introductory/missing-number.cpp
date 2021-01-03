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
    int n,k;
    cin >> n;
    vi used(n+1, 0);
    for (int i = 1; i<n; ++i) {
        cin >> k;
        used[k]++;
    }
    for (int i = 1; i<=n; ++i) {
        if (used[i] == 0) {
            cout << i << endl;
            break;
        }
    }
}
