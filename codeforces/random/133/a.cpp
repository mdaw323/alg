#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    string s;
    cin >> s;
    bool has_output = false;
    for (auto c : s) {
        if (c == 'H' || c == 'Q' || c == '9') {
            has_output = true;
        }
    }
    cout << (has_output ? "YES" : "NO") << endl;
}
