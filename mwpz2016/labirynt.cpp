#include <iostream>
using namespace std;

struct Vertex {
    int north=-1;
    int south=-1;
    int east=-1;
    int west=-1;
    int visited=-1;        
};

Vertex g[3000][3000];

void dfs(int x, int y, int d) {    
    if (g[x][y].visited == d) return;
    g[x][y].visited = d;
    if (g[x][y].north == d) dfs(x, y-1,d);
    if (g[x][y].south == d) dfs(x, y+1,d);
    if (g[x][y].east == d) dfs(x+1, y,d);
    if (g[x][y].west == d) dfs(x-1, y,d);
}


int main() {    
    int D, w, d, k;   
    char c;    
    cin >> D;
    
    while (D--) {             
        cin >> w >> d;
        int edges = 0;
        for (int i = 0; i<2*w +1; i++) {
            cin >> c;
            bool isEdge;
            if (c == 'P') isEdge = true; else isEdge = false;
            for (int j = 0; j< d + (i % 2);) {
                cin >> k;
                if (isEdge) {
                    for (int x=j; x<=j+k-1; ++x) {                        
                        if (i % 2 ==1) {                            
                            g[x-1][i/2].east = D;
                            g[x][i/2].west = D;
                        } else {
                            g[x][(i-1)/2].south = D;
                            g[x][(i-1)/2+1].north = D;                            
                        }
                        edges++;
                    }
                }
                j += k;
                isEdge = !isEdge;
            }
        } //wczytywanie danych - masakra - glowna trudnosc zadania
        
        int bridges = -1;
        
        for (int i = 0; i<w; i++) {
            for (int j = 0; j<d; j++) {
                if (g[i][j].visited !=D) {
                    bridges++;
                    dfs(i,j, D);                
                }
            }                        
        }                            
        cout << bridges + (edges + bridges) - (w*d-1) << endl;        
    }
    
    return 0;
}