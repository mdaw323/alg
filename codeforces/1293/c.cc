#include<bits/stdc++.h>

using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int n,q,r,c;
    cin >> n >> q;
    vector<vector<int>> m(2, vector<int> (n+2,0));
    int t = 0;
    for (int i = 0; i < q; i++) {
        cin >> r >> c;
        m[--r][c]^=1;
        for (int j = -1; j <=1; j++) {
            if (m[r^1][c+j] == 1) {
                if (m[r][c] == 1) {
                    t++;
                } else {
                    t--;
                }
            }
        }
        cout << (t==0 ? "Yes\n" : "No\n");
    }
}

