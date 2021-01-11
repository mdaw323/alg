#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
char dz[] = {'R', 'D', 'L', 'U'};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m, x, y, nx, ny;
    char z;
    string s;
    cin >> n >> m;
    pair<int, int> start, end;
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    vector<vector<int>> length(n, vector<int>(m, -1));
    vector<vector<tuple<int, int, char>>> parent(n, vector<tuple<int, int, char>>(m, {0, 0, 'X'}));
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (int j = 0; j < m; j++) {
            if (s[j] == 'A') {
                start = {i, j};
            } else if (s[j] == 'B') {
                end = {i, j};
            } else if (s[j] == '#') {
                visited[i][j] = true;
            }
        }
    }

    deque<pair<int, int>> q;
    q.push_back(start);
    length[start.first][start.second] = 0;
    visited[start.first][start.second] = true;
    while (!q.empty()) {
        tie(y, x) = q.front();
        q.pop_front();
        for (int i = 0; i < 4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[ny][nx]) {
                visited[ny][nx] = true;
                parent[ny][nx] = {y, x, dz[i]};
                length[ny][nx] = length[y][x] + 1;
                q.push_back({ny, nx});
            }
        }
    }
    string ans;
    tie(y, x) = end;
    if (length[y][x] > 0) {
        cout << "YES\n"
             << length[y][x] << endl;
        while (y != start.first || x != start.second) {
            tie(y, x, z) = parent[y][x];
            ans += z;
        }
        reverse(ans.begin(), ans.end());
        cout << ans << endl;
    } else {
        cout << "NO\n";
    }
}
