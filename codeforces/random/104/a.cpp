#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    int n;
    vector<int> chance = {0,4,4,4,4,4,4,4,4,4,15,4,0,0,0,0,0,0,0};
    cin >> n;
    n = max(0, n-10);
    cout << chance[n] << endl;
}
