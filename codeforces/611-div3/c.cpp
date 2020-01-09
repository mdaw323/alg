#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int n;
    cin >> n;

    vector<int> f(n+1);
    vector<bool> received(n+1);

    deque<int> g;
    deque<int> r;


    int s;

    for (int i = 1 ; i<= n; ++i) {
        cin >> s;
        f[i] = s;
        if (s > 0) {
            received[s] = true;
        } else {
            g.emplace_back(i);
        }
    }

    for (int i = 1; i<=n ; i++ ) {
        if (!received[i]) {
            r.emplace_back(i);
        }
    }
    int rr, gg;
    while (r.size() > 2) {
        rr = r.front();
        gg = g.front();
        r.pop_front();
        g.pop_front();
        if (rr == gg) {
            r.emplace_back(rr);
            rr = r.front();
            r.pop_front();
        }
        f[gg] = rr;
    }

    //~ printf("%d %d\n", g[0], g[1]);
    //~ printf("%d %d\n", r[0], r[1]);
    if (g[0] != r[0] && g[1] != r[1]) {
        f[g[0]] = r[0];
        f[g[1]] = r[1];
    } else {
        f[g[1]] = r[0];
        f[g[0]] = r[1];
    }



    assert(r.size() == g.size());

    for (int i = 1; i<= n; ++i) {
        cout << f[i] << " ";
    }
    cout << endl;

}
