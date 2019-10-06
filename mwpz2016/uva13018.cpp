#include <stdio.h>

int p[150];
int n,m;
char line[200];

int main() {
    int i,j;
    while (gets(line)) {
        sscanf(line, " %d%d", &n, &m);
        for (i = 0; i<41; i++) p[i] =0;
        for (i = 1; i<=n; i++)
            for (j = 1; j<= m; j++)
                p[i+j]++;
        m = 0;
        for (i = 0; i<41; i++) {
            if (m<p[i]) m = p[i];
        }
        for (i = 0; i<=40; i++) {
            if (m==p[i]) printf("%d\n",i);
        }
        
        printf("\n");
        n = 0;

    }
    
    return 0;
}