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
    vector<int> d(n);
    for (auto &x: d) {
        cin >> x;
    }
    sort(d.begin(),d.end());
    int cnt = 1;
    for (int i = 0; i<n-1; i++) {
        if (d[i]!= d[i+1]) {
            cnt++;
        }
    }
    cout << cnt << endl;
}
