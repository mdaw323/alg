#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N = 1e5 + 1;

vector<vector<int>> adj;
bool visited[N];
bool excluded[N];

int n, m;

void dfs(int s) {
    visited[s] = true;
    for (auto u : adj[s]) {
        if (!visited[u]) {
            excluded[u] = true;
            dfs(u);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    int u, v;
    adj.assign(n+1, vector<int>());
    for (int i = 0; i < m; i++) {
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (int i = 1; i <= n; i++) {
        if (!excluded[i]) {
            dfs(i);
        }
    }
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        if (!excluded[i]) {
            cnt++;
        }
    }

    cout << (cnt-1) << endl;
    for (int i = 2; i <= n; i++) {
        if (!excluded[i]) {
            cout << "1 " << i << endl;
        }
    }
}
