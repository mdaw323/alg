#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

const int MOD = 1e9 + 7;
int dp_p[1000001], dp_n[1000001];

int add(int a, int b) {
    int c = a + b;
    if (c > MOD) {
        c-=MOD;
    }
    return c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, t;
    cin >> t;

    dp_p[1] = 1;
    dp_n[1] = 1;
    for (int i = 2; i <= 1e6; i++) {
        int dpnn = add(dp_n[i - 1], dp_n[i - 1]);
        int dppp = add(dp_p[i - 1], dp_p[i - 1]);
        dp_n[i] = add(dpnn, dp_p[i - 1]);
        dp_p[i] = add(add(dppp, dppp), dp_n[i - 1]);
    }

    while (t--) {
        cin >> n;
        cout << add(dp_p[n], dp_n[n])<< endl;
    }
}
