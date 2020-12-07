#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    string a,b;
    cin >> a >> b;

    transform(a.begin(), a.end(), a.begin(), ::tolower);
    transform(b.begin(), b.end(), b.begin(), ::tolower);
    int cmp = a.compare(b);
    if (cmp < 0) {
        cmp = -1;
    } else if (cmp > 0 ) {
        cmp = 1;
    }
    cout << cmp << endl;

}
