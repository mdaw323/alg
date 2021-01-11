#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MX = 1e5 + 1;
vector<int> adj[MX];
int color[MX];
bool possible = true;

void dfs(int s, int c) {
    color[s] = c;
    int nc = (c == 1 ? 2 : 1);
    for (auto u : adj[s]) {
        if (color[u] == c) {
            possible = false;
        }
        if (color[u] == 0) {
            dfs(u, nc);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m, a, b;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    for (int i = 1; i <= n; ++i) {
        if (color[i] == 0) {
            dfs(i, 1);
        }
    }
    if (possible) {
        for (int i = 1; i <= n; i++) {
            cout << color[i] << " ";
        }
        cout << endl;
    } else {
        cout << "IMPOSSIBLE\n";
    }
}
