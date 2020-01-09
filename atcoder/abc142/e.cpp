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
const ll INF = 1e15 +7;

int main() {
    ios::sync_with_stdio(false);
    int N,M,b,s;
    cin >> N >> M;

    vector<int> K(M+1);
    vector<int> C(M+1);

    for (int i = 1 ; i<= M; i++) {
        cin >> C[i] >> b;
        int keys = 0;
        for (int j = 0; j < b; j++) {
            int dd;
            cin >> dd;
            keys |= 1 << (dd-1);
        }
        K[i] = keys;
    }

    int S = 1 << N;
    vector<ll> dp(S,INF);

    dp[0] = 0;
    for (int i = 1; i<=M; i++) {
        for (int j = 0; j < S; j++) {
            s = K[i] | j;
            dp[s] = min(dp[s],dp[j] + C[i]);
        }
    }
    if (dp[S-1] == INF) {
        dp[S-1] = -1;
    }

}
