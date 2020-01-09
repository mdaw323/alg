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

    ll a,b;
    cin >> a >> b;

    int cnt = 1;

    ll x = 2;

    while (a>1 && b > 1 && x * x <= max(a,b)) {
        //~ debug(x,max(a,b));
        if ( a % x == 0 && b % x == 0) {
            //~ debug(x);
            cnt++;
            while (a % x == 0)
                a /=x;
            while (b % x == 0)
                b /=x;
        }
        x++;
    }
    if (a > 1 && b > 1 ) {
        if (__gcd(a,b) >1) {
            cnt++;
        }
    }
    cout << cnt;

}
