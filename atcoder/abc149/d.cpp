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

int main() {
    ios::sync_with_stdio(false);
    int N,K,R,S,P;
    string T;
    cin >> N >> K >> R >> S >> P;
    cin >> T;
    vector<int> C = {R,P,S};
    vector<int> M (N+1);
    for (int i =0 ; i<N; i++ ) {
        if (T[i] == 'r') {
            M[i+1] = 0;
        } else if (T[i] == 's') {
            M[i+1] = 2;
        } else {
            M[i+1] = 1;
        }
    }
    vector<vector<int>> dp(N+1, vector<int> (3));
    for (int i = 1; i <= K; i++ ) {
        int m = max({dp[i-1][0], dp[i-1][1], dp[i-1][2]});
        for (int j = 0; j <3; j++ ) {
            if (M[i] == ((j + 1) % 3)) {
                dp [i][j] = m ;//- C[j];
            } else if (M[i] == j) {
                dp [i][j] = m;
            } else {
                dp [i][j] = m + C[j];
            }
        }
    }
    for (int i = K+1; i <= N; i++) {
        int m1 = max({dp[i-1][0], dp[i-1][1], dp[i-1][2]});
        int mk = max({dp[i-K][0], dp[i-K][1], dp[i-K][2]});
        for (int j = 0; j<3; j++ ) {
            int dd = max(dp[i-K][(j+1) %3], dp[i-K][(j+2) %3]);
            if (M[i] == j) {
                dp[i][j] = m1 - (mk - dd);
            } else if (M[i] == ((j+1) % 3)) {
                dp[i][j] = m1 - (mk - dd) ;//-C[j]; 
            } else {
                dp[i][j] = m1 - (mk - dd) + C[j];
            }
        }
    }
    for (int j = 0; j<3; j++ ) {
        for (int i = 0; i<=N; i++) {
            cerr << dp[i][j] << " ";
        }
        cerr << "\n";
    }
    cout << max({dp[N][0], dp[N][1], dp[N][2] });
}
