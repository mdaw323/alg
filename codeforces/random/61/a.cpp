#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    string s1, s2;
    cin >> s1 >> s2;

    for (int i = 0; i<s1.length(); i++) {
        cout << (s1[i] != s2[i] ? 1 : 0);
    }
    cout << endl;
}
