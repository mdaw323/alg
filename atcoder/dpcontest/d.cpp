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
    int N, W;
    scanf("%d%d", &N, &W);
    int w, v ;
    
    vector<ll> dp(W+1);
    for (int i = 1; i<= N; i++) {
        scanf("%d %d", &w, &v);
        for (int j = W; j>=w; j--) {
            dp[j] = max(dp[j], dp[j-w] + v);
        }
    }

    printf("%lld\n", dp[W]);
}
