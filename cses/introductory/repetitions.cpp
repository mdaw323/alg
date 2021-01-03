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
    string s;
    cin >> s;
    int n = 1,m = 1;

    for (int i = 1; i<(int)s.size(); i++) {
        if (s[i-1] == s[i]) {
            n++;
            m=max(m,n);
        } else {
            n = 1;
        }
    }
    cout << m << endl;
}
