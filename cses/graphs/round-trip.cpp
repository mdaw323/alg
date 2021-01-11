#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MX = 1e5 + 1;
vector<int> adj[MX];
bool visited[MX];
int parent[MX];
int cycle = -1;

void dfs(int s) {
    visited[s] = true;
    for (auto u : adj[s]) {
        if (cycle > 0) return;
        if (visited[u] && parent[s] != u) {
            parent[u] = s;
            cycle = s;
            return;
        } else if ( !visited[u]) {
            parent[u] = s;
            dfs(u);
        }
    }
}

vector<int> find_cycle(int s) {
    int j = parent[s];
    vector<int> ans;
    ans.push_back(s);
    while (j != s) {
        ans.push_back(j);
        j = parent[j];
    }
    ans.push_back(j);
    return ans;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m, a, b;
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    for (int i = 1; i<=n; i++) {
        if (!visited[i] && cycle <0) {
            dfs(i);
        }
    }

    if (cycle > 0) {
        vector<int> ans = find_cycle(cycle);
        cout << ans.size() << endl;
        for (auto i : ans) {
            cout << i << " ";
        }
        cout << endl;
    } else {
        cout << "IMPOSSIBLE\n";
    }
}
