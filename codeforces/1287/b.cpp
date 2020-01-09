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
    int n,k;
    cin >> n >> k;
    vector<string> V(n);
    string s;
    unordered_set<string> M;
    for (int i = 0; i< n; i++) {
        cin >> V[i];
        M.insert(V[i]);
    }
    char z = 'S' + 'E' + 'T';
    int cc = 0;
    for (int i = 0; i< n; i++) {
        for (int j = i+1; j<n; j++) {
            s = "";
            for (int l = 0; l<k; l++) {
                if (V[i][l] == V[j][l]) {
                    s+=V[i][l];
                } else {
                    s+= z - V[i][l] - V[j][l];
                }
            }
            if (M.find(s) != M.end()) {
                cc++;
            }
        }
    }
    cout << cc / 3 << "\n";

}
