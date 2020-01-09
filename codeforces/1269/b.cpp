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

int sub_modulo(int a, int b, int m) {
    int r = a-b;
    return r >= 0 ? r : r+m;
}

int add_modulo(int a, int b, int m) {
    int r = a+b;
    return r < m ? r : r-m;
}

int main() {
    ios::sync_with_stdio(false);
    int n,m;
    cin >> n >> m;
    vector<int> a(n), b(n);

    for (auto &x : a) {
        cin >> x;
    }
    for (auto &x : b) {
        cin >> x;
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    for (auto &x : a) {
        cerr << x << " ";
    }
    cerr << endl;
    for (auto &x : b) {
        cerr << x << " ";
    }
    cerr << endl;

    int minx = m;
    for (int k = 0; k <n; k++) {
        bool check = true;
        // a[i] + x mod m = b[i]
        // x = b[i] -a[i]
        int x = sub_modulo(b[k], a[0],m);

        for (int i = 1; i<n; i++) {
            if (sub_modulo(b[add_modulo(k,i,n)], a[i],m) != x) {
                check = false;
                break;
            }
        }

        if (check) {
            minx = min(minx, x);
        }
        debug(k,x,check, minx);
    }
    cout << minx << endl;
}
