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
    int k,r= 0;
    ll suma = 0;
    int odd = 0;
    int even = 0;
    for (int i = 0; i< n; i++) {
        cin >> k;
        suma += k / 2;
        r = k % 2;
        if (r == 1) {
            if (i % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
    }

    cout << suma + min(odd,even) << "\n";


}
/*

4
3 2 2 1

4

3
5 4 3
*/
