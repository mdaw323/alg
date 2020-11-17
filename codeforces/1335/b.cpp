#include <bits/stdc++.h>
using namespace std;

#define debug(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); err(_it, args); }
void err(istream_iterator<string> it) {}
template<typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args) {
    cerr << "["<< *it << " = " << a << "]"<< endl;
    err(++it, args...);
}
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int t, n, a, b, k, diff;
    cin >> t;
    while (t--) {
        vector<int> C(26);
        vector<int> V(2001, -1);
        cin >> n >> a >> b;
        k = 0;
        diff = 1;        
        V[0] = 0;
        C[V[0]]++;
        cout << char('a' + 0);
        for (int i = 1; i<n; i++) {
            if (i+1 > a) {
                C[V[i-a]]--;
                if (C[V[i-a]] == 0) {
                    diff--;
                }
            }
            if (diff < b) {
                k = (k+1) % 26;
                diff++;                
            }
            V[i] = k;
            cout << char('a' + k);
            C[k]++;            
        }
        cout << "\n";
    }
}
