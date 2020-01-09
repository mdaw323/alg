#include <bits/stdc++.h>
using namespace std;

#define debug(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); err(_it, args); }
void err(istream_iterator<string> it) {}
template<typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args) {
    cerr << "["<< *it << " = " << a << "]"<< endl;
    err(++it, args...);
}
using ll = long long;
const int INF = 1e9;


int main() {
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    vector<int> A(n+1);
    int odds = 0;
    for (int i = 1; i<=n; i++) {
        cin >> A[i];
        if (A[i] %2 !=0) {
            odds++;
        }
    }
    odds = (n+1) / 2 - odds;

    // dp[i][j][p] = minimalna złożoność w przedziale 0..i przy wykorzystaniu j nieparzystych liczb
    // zakładając, że ostatnia liczba jest parzysta (p == 0) lub nieparzysta (p ==1)

    vector<vector<vector<int>>> dp (n+1, vector<vector<int>>(odds+1, vector<int>(2,INF)));

    dp[0][0][0] = dp[0][0][1] = 0;
    for (int i = 1; i<= n; i++) {
        int pp = A[i] % 2;
        for (int j = 0; j<= odds; j++) {
            if (A[i] == 0) { //trzeba wybrać
                if (j > 0) { //wybieram nieparzystą
                    dp[i][j][1] = min( dp[i-1][j-1][0] + 1, dp[i-1][j-1][1]);
                }
                dp[i][j][0] = min( dp[i-1][j][0], dp[i-1][j][1] + 1);
            } else { //jeśli zmiana parzystości to dodaj 1 do kosztu
                dp[i][j][pp] = min(dp[i-1][j][pp] , dp[i-1][j][1-pp] + 1);
            }
        }
    }
    cout << min (dp[n][odds][0], dp[n][odds][1]) << "\n";
}
