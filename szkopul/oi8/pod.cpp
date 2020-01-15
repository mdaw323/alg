#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

struct way {
    int d, f, r, t;
};

int main() {
    ios::sync_with_stdio(false);
    int n,k,x,y,g,m;
    cin >> n >> k >> x >> y >> g >> m;
    vector<int> P(n+1), R(n+1);
    vector<vector<way>> E(n+1, vector<way>(0) );
    for (int j = 1; j <= k; j++) {
        int s,c,seq = 0;
        cin >> s >> c;
        for (int l = 1; l<=s; l++) {
            cin >> P[l];
        }
        for (int l = 1; l<s; l++) {
            cin >> R[l];
            way w = {P[l+1], c, seq % c, R[l]};
            E[P[l]].emplace_back(w);
            seq+=R[l];
        }
        seq = 0;
        for (int l = s-1; l>=1; l--) {
            way w = {P[l], c, seq % c, R[l]};
            E[P[l+1]].emplace_back(w);
            seq += R[l];
        }
    }

    vector<int> D (n+1, INF);
    priority_queue< pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > Q;
    Q.push({g*60+m, x});

    int t,v,c;
    while(Q.size() > 0) {
        tie(t,v) = Q.top();
        Q.pop();
        if (D[v] > t) {
            D[v] = t;
            if (v == y) {
                break;
            }
            for (way w : E[v]) {
                int wait = (w.f + w.r-t%w.f) % w.f;
                c = wait + w.t + t;
                if (D[w.d] > c) {
                    Q.push({c, w.d});
                }
            }
        }
    }
    cout << D[y] % 1440 / 60 << " " << D[y] % 60 << endl ;
}
