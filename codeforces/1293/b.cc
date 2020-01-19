#include<bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    double d = 0.0;
    while (n>=1) {
        d+= 1.0 / ((double)n);
        n--;
    }
    cout << d;
}
