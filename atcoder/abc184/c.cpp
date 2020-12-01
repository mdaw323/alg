#include <bits/stdc++.h>
using namespace std;

using ll = long long;

bool can_jump(ll a, ll b, ll c, ll d)
{
    return a + b == c + d ||
           a - b == c - d ||
           abs(a - c) + abs(b - d) <= 3;
}

int main()
{
    ios::sync_with_stdio(false);
    ll a, b, c, d, x, y;
    cin >> a >> b >> c >> d;
    if (a == c && b == d)
    {
        cout << "0" << endl;
    }
    else if (can_jump(a, b, c, d))
    {
        cout << "1" << endl;
    }
    else
    {
        for (x = a - 3; x <= a + 3; x++)
        {
            for (y = b - 3; y <= b + 3; y++)
            {
                if (can_jump(a, b, x, y) &&
                    can_jump(x, y, c, d))
                {
                    cout << "2" << endl;
                    return 0;
                }
            }
        }
        if ((a + b) % 2 == (c + d) % 2)
        {
            cout << "2" << endl;
        }
        else
        {
            cout << "3" << endl;
        }
    }
}