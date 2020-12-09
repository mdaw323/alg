#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int t;
    ll x,y,k, t1, t2;
    cin >> t;
    while (t--) {
        cin >> x >> y >> k;
        t2 = k;
        t1 = (k + k * y -1) / (x-1);
        if ((k + k * y  -1) % (x-1) != 0) {
            t1++;
        }
        cout << t1 + t2<< endl;
    }
}
