#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main()
{
    ios::sync_with_stdio(false);
    int N, X;
    string S;
    cin >> N >> X;
    cin >> S;
    for (char c : S)
    {
        if (c == 'x')
        {
            X = max(0, X - 1);
        }
        else
        {
            X++;
        }
    }
    cout << X << endl;
}