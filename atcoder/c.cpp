#include<stdio.h>
#include<vector>

using namespace std;

int main() {
    int N, a, b, c;

    scanf("%d", &N);

    vector<vector<int>> dp(3, vector<int>(N, 0));

    scanf ("%d%d%d", &a, &b, &c);
    dp[0][0] = a;
    dp[1][0] = b;
    dp[2][0] = c;

    for (int i = 1; i<N; i++) {
        scanf ("%d%d%d", &a, &b, &c);
        dp[0][i] = max(dp[1][i-1] , dp[2][i-1] ) + a;
        dp[1][i] = max(dp[0][i-1] , dp[2][i-1] ) + b;
        dp[2][i] = max(dp[1][i-1] , dp[0][i-1] ) + c;
    }

    int m = max(max(dp[0][N-1], dp[1][N-1]), dp[2][N-1]);
    printf ("%d", m);
    return 0;
}

