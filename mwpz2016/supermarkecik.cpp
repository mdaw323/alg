#include <cstdio>  

int main() 
{
        int D;

        scanf("%d\n",&D);
        char S[2000001];
        while (D--) {
                int jj=0;
                char c;
                do {
                        c = getchar_unlocked();
                        S[jj++] = c;
                } while (c!='\n');
                int j = 0;
                bool res = true;
                do {
                        c = getchar_unlocked();
                        if (c == '\n') {
                                break;
                        }

                        while(j < jj && c != S[j]) {
                                j++;
                        }
                        if (j >= jj) {
                                res = false;
                        }
                        j++;
                } while (c != '\n');
                if (res) {
                        printf("TAK\n");
                } else {
                        printf("NIE\n");
                }

        } 
        return 0;
}
