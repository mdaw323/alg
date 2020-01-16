#include<bits/stdc++.h>
using namespace std;

int B[200][200];
char s[200];
int main() {
    int n,m;

    scanf("%d%d", &n, &m);
    for (int i = 0; i<n; i++) {
        scanf("%s",s);
        for (int j = 0; j< m; j++) {
            B[i][j] = s[j] - '0';
        }
    }
    deque<pair<int,int>> Q;
    for (int i = 0; i< n; i++) {
        for (int j = 0; j<m; ++j) {
            if (B[i][j] == 1) {
                Q.push_back({i,j});
                B[i][j] = 0;
            } else {
                B[i][j] = -1;
            }

        }
    }
    int a, b, x, y;
    vector<int> dx = {1,0,-1,0};
    vector<int> dy = {0,1,0,-1};
    while (!Q.empty()) {
        tie(a,b) = Q.front();
        Q.pop_front();
        for (int i = 0; i<4; i++) {
            x = a + dx[i];
            y = b + dy[i];
            if (x >=0 && y >=0 && x < n && y < m && B[x][y] == -1) {
                Q.push_back({x,y});
                B[x][y] = B[a][b] + 1;
            }
        }
    }

    for (int i = 0; i< n; i++) {
        for (int j = 0; j <m; j++) {
            if (j > 0) printf(" ");
            printf("%d", B[i][j]);
        }
        printf ("\n");
    }

}

