#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int main()
{
    ios::sync_with_stdio(false);
    int t, x;

    cin >> t;
    while (t--)
    {
        cin >> x;
        int k = 0;
        int s = 0;
        while (s < x)
        {
            k++;
            s += k;
        }

        cout << ((s == x+1) ? k+1 : k) << endl;
    }
}