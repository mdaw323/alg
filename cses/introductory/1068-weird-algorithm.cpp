#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n;
    cin >> n;
    cout << n;
    while (n!=1) {
        if (n%2==0) {
            n /=2;
        } else {
            n = n*3 +1;
        }
        cout << " " << n;
    }
    cout << endl;
}
