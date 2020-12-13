#include <bits/stdc++.h>
using namespace std;
using ll = long long;

class Graph {
    int n;
    vector<set<int>> adj;
    vector<int> parent;
    vector<int> cycle;
    vector<bool> visited;
    vector<int> rank;

   public:
    Graph(int n1) {
        n = n1;
        adj = vector<set<int>>(n);
        parent = vector<int>(n);
        rank = vector<int>(n);
        visited = vector<bool>(n);
    }
    void addEdge(int u, int v) {
        adj[u].insert(v);
        adj[v].insert(u);
    }

    void mark_cycle(int p, int v) {
        if (cycle.begin() == cycle.end()) {
            cycle.push_back(v);
            int x = p;
            while (x != v) {
                cycle.push_back(x);
                x = parent[x];
            }
        }
    }

    int dfs_visit(int p, int v) {
        if (visited[v]) {
            mark_cycle(p, v);
            return 0;
        }
        visited[v] = true;
        parent[v] = p;
        int cnt = 1;
        for (auto e : adj[v]) {
            if (e != p) {
                cnt += dfs_visit(v, e);
            }
        }
        return cnt;
    }

    int dfs(int s) {
        rank[s] = dfs_visit(s, s);
        return rank[s];
    }

    vector<int> find_cycle() {
        cycle = vector<int>();
        dfs(0);
        return cycle;
    }

    void remove_cycle_edges() {
        int a, b;
        for (int i = 0; i < (int)cycle.size(); i++) {
            a = cycle[i];
            b = cycle[(i + 1) % cycle.size()];
            adj[a].erase(b);
            adj[b].erase(a);
        }
        visited = vector<bool>(n, false);
    }

    void printGraph() {
        for (int i = 0; i < n; i++) {
            cout << i << " r(" << rank[i] << ") v(" << (int)(visited[i]) << ") -> ";
            for (auto j : adj[i]) {
                cout << j << " ";
            }
            cout << endl;
        }
    }
};

void solve() {
    int n, e, v;
    cin >> n;
    Graph g = Graph(n);
    for (int i = 0; i < n; i++) {
        cin >> e >> v;
        g.addEdge(e - 1, v - 1);
    }
    // g.printGraph();
    auto cycle = g.find_cycle();
    // cout << "cycle";
    // for (auto c : cycle) {
    //     cout << " " << c;
    // }
    // cout << endl;

    g.remove_cycle_edges();
    ll cnt = 0;
    for (auto c : cycle) {
        ll k = g.dfs(c);
        // cout << c << " " <<k << endl;
        cnt += k * (k - 1) / 2;
        cnt += (n - k) * k;
    }
    cout << cnt << endl;
    // g.printGraph();
}

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
