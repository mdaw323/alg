#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MX = 1001;

bool v[MX][MX];
tuple<int, int, char> p[MX][MX];
vector<vector<int>> d(MX, vector<int>(MX, -1));

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
char dz[] = {'R', 'D', 'L', 'U'};
int n, m;

void bfs(vector<pair<int, int>> monsters, pair<int, int> s) {
    queue<pair<int, int>> q, mq;
    int x, y;
    for (int i = 0; i < (int)monsters.size(); i++) {
        tie(x, y) = monsters[i];
        mq.push({x, y});
        v[x][y] = true;
    }

    tie(x, y) = s;
    q.push({x, y});
    d[x][y] = 0;
    v[x][y] = true;
    while (!q.empty()) {
        for (int i = mq.size(); i > 0; --i) {
            tie(x, y) = mq.front();
            mq.pop();
            for (int j = 0; j < 4; j++) {
                int nx = dx[j] + x;
                int ny = dy[j] + y;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !v[nx][ny]) {
                    mq.push({nx, ny});
                    v[nx][ny] = true;
                }
            }
        }
        for (int i = q.size(); i > 0; --i) {
            tie(x, y) = q.front();
            q.pop();
            for (int j = 0; j < 4; j++) {
                int nx = dx[j] + x;
                int ny = dy[j] + y;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !v[nx][ny]) {
                    q.push({nx, ny});
                    v[nx][ny] = true;
                    d[nx][ny] = d[x][y] + 1;
                    p[nx][ny] = {x, y, dz[j]};
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    pair<int, int> me;
    vector<pair<int, int>> mon;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            if (s[j] == '#') {
                v[j][i] = true;
            } else if (s[j] == 'A') {
                me = {j, i};
            } else if (s[j] == 'M') {
                mon.push_back({j, i});
            }
        }
    }
    bfs(mon, me);

    pair<int, int> bd = {0, 0};
    for (int i = 0; i < m; i++) {
        if (d[i][0] >= 0 && d[i][0] <= n * m) {
            bd = {i, 0};
        }
        if (d[i][n - 1] >= 0 && d[i][n - 1] <= n * m) {
            bd = {i, n - 1};
        }
    }

    for (int j = 0; j < n; j++) {
        if (d[0][j] >= 0 && d[0][j] <= n * m) {
            bd = {0, j};
        }
        if (d[m - 1][j] >= 0 && d[m - 1][j] <= n * m) {
            bd = {m - 1, j};
        }
    }
    int x, y, mx, my, c;
    tie(mx, my) = me;
    tie(x, y) = bd;
    if (d[x][y] > -1) {
        cout << "YES\n"
             << d[x][y] << endl;
        string ans;
        while (d[x][y] != 0) {
            tie(x, y, c) = p[x][y];
            ans += c;
        }
        reverse(ans.begin(), ans.end());
        cout << ans<< endl;
    } else {
        cout << "NO\n";
    }
}
