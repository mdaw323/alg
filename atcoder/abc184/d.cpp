#include <bits/stdc++.h>
using namespace std;

using ll = long long;

vector<vector<vector<double>>> dp(101, vector<vector<double>>(101, vector<double>(101, -1)));

double count(int i, int j, int k)
{
    if (i == 100 || j == 100 || k == 100)
    {
        return 0;
    }
    else if (dp[i][j][k] > -1)
    {
        return dp[i][j][k];
    }
    else
    {
        double s = i + j + k;
        dp[i][j][k] = (double)i / s * (count(i + 1, j, k) + 1) +
                      (double)j / s * (count(i, j + 1, k) + 1) +
                      (double)k / s * (count(i, j, k + 1) + 1);
        return dp[i][j][k];
    }
}

int main()
{
    ios::sync_with_stdio(false);

    int a, b, c;
    cin >> a >> b >> c;

    dp[0][0][0] = 0;

    cout.precision(10);

    cout << fixed << count(a, b, c) << endl;
}