#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int N;
vector<vector<int>> T;
vector<vector<int>> G;
vector<bool> used;
vector<int> order, comp;
vector<bool> assignment;

void generateTraverse() {
    for (int i = 0; i<N; i++) {
        for (int j : G[i]) {
            T[j].push_back(i);
        }
    }
}

void dfs1(int v) {
    used[v] = true;
    for (int u : G[v]) {
        if (!used[u]) {
            dfs1(u);
        }
    }
    order.push_back(v);
}

void dfs2(int v, int c) {
    comp[v] = c;
    for (int u : T[v]) {
        if (comp[u] == -1) {
            dfs2(u, c);
        }
    }
}

bool solve_2SAT() {
    generateTraverse();
    used.assign(N,false);
    comp.assign(N, -1);
    assignment.assign(N/2,false);
    for (int i = 0; i < N; ++i) {
        if (!used[i]) {
            dfs1(i);
        }
    }
    for (int i = 0, j = 0; i < N; ++i) {
        int v = order[N-i-1];
        if (comp[v] == -1) {
            dfs2(v, j++);
        }
    }
    for (int i = 0; i < N; i+=2) {
        if (comp[i] == comp[i+1]){
            return false;
        }
        assignment[i/2] = comp[i] > comp[i+1];
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    int n, m, a, b, p;
    cin >> n >> m;
    p = 2*n;
    N = 2*p;
    //x = 2i, 
    //~x = 2i+1i
    G.assign(N,vector<int>(0));
    T.assign(N,vector<int>(0));
    for (int i = 0; i<n; i++) {
        // a or b <=> ~a => b and ~b => a
        a = 2 * i ;
        b = 2 * i + 1;
        G[2*a+1].push_back(2*b);
        G[2*b+1].push_back(2*a);
    }
    for (int i = 0; i<m; i++) {
        cin >> a >> b;
        a--;
        b--;
        //~(a and b) <=> a => ~b and b => ~a
        G[2*a].push_back(2*b+1);
        G[2*b].push_back(2*a+1);
    }
    if (!solve_2SAT()) {
        cout << "NIE\n";
    } else {
        for (int i = 0; i < n; i++) {
            assert (assignment[2*i] || assignment[2*i+1]);
            cout << (assignment[2*i] ? (2*i+1) : (2*i+2)) << "\n";
        }
    }
    
}
