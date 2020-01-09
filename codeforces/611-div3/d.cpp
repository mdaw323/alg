#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = 1e15 + 7;
int main() {
    ios::sync_with_stdio(false);
    int n,m;
    cin >> n >> m;
    vector<ll> y(m), x(n), l(n), r(n);
    deque<pair<int,int>> Q;

    for (int i = 0 ; i<n; i++) {
        cin >> x[i];
    }
    sort(x.begin(), x.end());
    l[0] = INF;
    r[n-1] = INF;
    for (int i = 0; i<n-1; i++) {
        ll d = x[i+1] - x[i] -1;
        ll h = d / 2;
        r[i] = h;
        l[i+1] = d -h;
    }

    for (int i = 0 ;i< n; i++) {
        if (l[i] > 0 || r[i] > 0) {
            Q.emplace_back(make_pair(i,1));
        }
    }

    ll sum_of_distance = 0;
    ll distance;
    int i;
    while (m > 0) {
        tie(i,distance) = Q.front();
        Q.pop_front();
        if (l[i] >= distance) {
            m--;
            y[m] = x[i] - distance;
            sum_of_distance +=distance;
        }
        if (m == 0) break;
        if (r[i] >= distance) {
            m--;
            y[m] = x[i] + distance;
            sum_of_distance +=distance;
        }

        if (l[i] > distance || r[i] > distance) {
            Q.emplace_back(make_pair(i,distance+1));
        }

    }

    cout << sum_of_distance << "\n";
    for (auto t : y) {
        cout << t << " ";
    }
    cout << "\n";
}
