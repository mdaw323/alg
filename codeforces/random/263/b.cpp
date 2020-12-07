#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int x, ans = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0 ; j< 5; j++) {
            cin >> x;
            if (x == 1) {
                ans = abs(i-2) + abs (j-2);
            }
        }
    }
    cout << ans << endl;
}
