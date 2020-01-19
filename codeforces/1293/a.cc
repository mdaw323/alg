#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int t, n, s, k, r;
    cin >>t ;
    while (t--) {
        vector<bool> left(2001, false), right(2001, false);
        
        cin >> n >> s >>k;

        for (int i = 0; i<k; i++ ) {
            cin >> r;
            r = r - s;
            if (r >=0 && r<=2000) {
                right[r] = true;
            } 
            if (r <=0 && r>=-2000) {
                left[-r] = true;
            }
        }
        for (int i = 0; i<=2000; i++) {
            if ((s+i <= n && !right[i]) || (s-i >= 1 && !left[i])) {
                cout << i << "\n";
                break;
            } 
        }
    }
}
