#include <iostream>
#include <math.h>
#include <cstring>

using namespace std;

static const int MI = 1000010;
static const unsigned int MOD = 1000000007;
unsigned int x[MI][11];
unsigned int z[2][10];

void convert_array(char *t, int l) {    
    char tmp;
    for (int i = 0; i < (l+1)/2 ; i++) {
        tmp = t[l-1-i] - '0';
        t[l-1-i] = t[i] - '0';
        t[i] = tmp;
    }
}

void initialize_counting_table() {
    for (int i = 0 ; i< 10; i++) 
        x[0][i] = 1;
    x[0][10] = 9;
        
    for (int i = 1; i < MI; i++) {
        x[i][0] = x[i-1][1];
        x[i][9] = x[i-1][8];
        for (int j = 1; j<=8; j++) 
            x[i][j] = (x[i-1][j-1] + x[i-1][j+1]) % MOD;
        for (int j = 1; j<10;j++) {
            x[i][10] += x[i][j];            
            x[i][10] %= MOD;
        }
        x[i][10]+=x[i-1][10];
        x[i][10] %= MOD;
    }
}

unsigned int count_with_limit(char *t, int l) {
    unsigned int s = t[0];
    for (int i = 0 ; i<= t[0]; i++) 
        z[0][i] = 1;
    for (int i = t[0]+1 ; i< 10; i++) 
        z[0][i] = 0;
    for (int i =1; i<l; i++) {
        s = x[i-1][10];
        
        for (int j = 0; j < t[i]; j++) 
            z[i % 2][j] = x[i][j];
        
        for (int j = t[i]; j < 10; j++) 
            z[i%2][j] = 0;
        if (t[i] > 0) 
            z[i%2][t[i]] += z[(i-1)%2][t[i]-1];
        if (t[i] < 9) 
            z[i%2][t[i]] += z[(i-1)%2][t[i]+1];
        z[i%2][t[i]] %= MOD;
        
        for (int j = 1; j < 10; j++) {
            s += z[i%2][j];
            s%=MOD;
        }
        s%=MOD;
    }
    return s;
}

int main() {
    int D;
    char a[MI], b[MI];
    initialize_counting_table();
    cin>>D;
    while (D--) {
        cin>>a>>b;
        int a_length = strlen(a);
        int b_length = strlen(b);
        convert_array(a, a_length);
        unsigned int ca = count_with_limit(a, a_length);
        convert_array(b, b_length);
        unsigned int cb = count_with_limit(b, b_length);
        bool addOne = true;
        for (int i = 1; i<a_length; i++) {
            if (a[i-1] - a[i] == 1 || a[i-1] - a[i] == -1) {
            } else {
                addOne = false;
                break;
            }
        }
        unsigned int res = MOD + cb - ca;
        if (addOne) {
            res++;
        }
        res %= MOD;
            
        cout << res << endl;
    }

    return 0;
}