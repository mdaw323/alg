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
    int t,k;
    cin >> t;
    while(t--) {
        cin >> k;
        char A[k+1];
        cin >> A;
        int maxm = 0;
        int m = 0;
        bool initial = true;
        for (int i = 0; i < k; i++) {
            if (A[i] == 'A') {
                initial = false;
                maxm = max (m, maxm);
                m = 0;
            } else {
                if (!initial)
                    m++;
            }
        }
        maxm = max(m,maxm);

        cout << maxm << "\n";

    }
}
