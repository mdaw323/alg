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
    int n;
    cin >> n;
    bool prime = false;
    while (!prime) {
        prime = true;
        for (int i = 2; i*i <= n; i++ ) {
            if (n % i == 0) {
                prime = false;
                break;
            }
        }
        if (prime) {
            break;
        }
        n++;
    }
    cout << n;

}
