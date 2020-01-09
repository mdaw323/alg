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
    cin >> n >>k;
    char s[n+1];
    cin >> s;

    bool add_one = false;
    for (int i = k; i<n; i++) {
        if (s[i] != s[i % k]) {
            if (s[i %k] > s[i]) {
                break;
            } else {
                add_one = true;
                break;
            }
        }
    }

    debug(add_one);
    if (add_one) {
        int i = k-1;

        while ( i>=0 ) {
            debug(i);
            if (s[i] == '9') {
                s[i] = '0';
                i--;
            } else {
                s[i] = s[i] + 1;
                break;
            }
        }
    }

    cout << n << "\n";
    for (int i = 0; i< n; i++) {
        cout << s[i % k] - '0';
    }
    cout << "\n";


}
