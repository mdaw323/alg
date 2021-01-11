#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MX = 1e5 + 1;
vector<int> adj[MX];
bool visited[MX];
int dist[MX];
int parent[MX];

void bfs(int s) {
    queue<int> q;
    q.push(s);
    dist[s] = 0;
    parent[s] = s;
    visited[s] = true;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (auto v : adj[u]) {
            if (!visited[v]) {
                q.push(v);
                visited[v] = true;
                dist[v] = dist[u] + 1;
                parent[v] = u;
            }
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
    bfs(n);
    if (dist[1] > 0) {
        cout << dist[1]+1 << "\n1";
        int i = 1;
        while (i != parent[i]) {
            cout << " " << parent[i];
            i = parent[i];
        }
        cout << endl;
    } else {
        cout << "IMPOSSIBLE\n";
    }
}
