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
    cin >> n;
    vector<int> v(n+1);
    for (int i = 1 ; i<= n; i++ ) {
        cin >> k;
        v[k] = i;
    }

    for (int i = 1 ; i<= n; i++ ) {
        cout << v[i] << " ";
    }

}
