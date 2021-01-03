#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, x;
    cin >> n >> x;
    vi weights(n);
    for (auto &a : weights) {
        cin >> a;
    }
    int N = 1 << n;
    vi min_rides(N, n + 1), can_take(N, x);
    min_rides[0] = 1;

    for (int s = 1; s < N; ++s) {
        for (int k = 0; k < n; ++k) {
            if (s & 1 << k) {
                int prev = s ^ (1 << k);
                int take = 0, rides = 0;
                if (can_take[prev] >= weights[k]) {
                    // cerr << "take " << s <<" "<< prev;
                    take = can_take[prev] - weights[k];
                    rides = min_rides[prev];
                } else {
                    // cerr << "new " << s <<" "<< prev;
                    take = x - weights[k];
                    rides = min_rides[prev] + 1;
                }
                if (rides < min_rides[s] || (rides == min_rides[s] && take>can_take[s])) {
                    min_rides[s] = rides;
                    can_take[s] = take;
                }
                // cerr << " min: " << min_rides[s] << " " << can_take[s] << endl;
            }
        }
    }
    // for (int i = 0; i < N; i++) {
    //     cerr << i << " " << min_rides[i] << " " << can_take[i] << endl;
    // }
    cout << min_rides[N - 1] << endl;
}
