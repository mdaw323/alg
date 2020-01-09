#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int t,n,k;
    cin >> t;
    while(t--) {
        cin >> n >> k;
        cout << (n / k) * k  + min(k/2, n % k) << "\n";

    }
}
