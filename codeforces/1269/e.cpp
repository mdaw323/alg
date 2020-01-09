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
    int n,l, s, suma=0;
    cin >> n;
    vector<int> A(n+1);

    for (int k = 0; k < n; k++) {
        cin >> l;

        s = 0;
        int j= l;
        while (j >0) {
            s += A[j];
            j-= j & -j;
        }
        j = l;
        while (j< n+1){
            A[j]++;
            j+= j & -j;
        }
        suma += k-s;
        cout << suma << " ";
    }
    cout << "\n";
}
