#include <iostream>

using namespace std;

int W[51] = {9,3,11,6,7,3,3,3,3,29,16,4,4,20,11,6,55,6,9,15,8,9,8,4,10,11,16,10,6,10,3,5,6,4,14,29,5,18,7,7,20,4,38,11,6,3,12,13,5,10,3};
int V[51][1001];
int K[1001];
int K2[1001];

int main() {
    int N, s, k;    
    cin >> N;
    while (N--) {
        cin >> s >> k;
        V[s-1][k]++;
        V[s-1][0]++;
    }
        
     for (int i =0; i<51; i++) {
        int mi = 1;
        
        bool alone = true;
        for (int j = 2; j<=1000; j++) {
            if (V[i][j] > V[i][mi]) {
                mi = j;
                alone = true;
            } else if (V[i][j] == V[i][mi]) {
                alone = false;
            }
        }
        
        if (alone && i != 23 && i != 31) {
            K[mi]+=W[i];
        }
        if (alone && i != 8) {
            K2[mi]++;            
        }
    }
    for (int i = 1; i<=1000; i++) {
        K[i] += (float)V[23][i] * (float)W[23] / (float)V[23][0];
        K[i] += (float)V[31][i] * (float)W[31] / (float)V[31][0];
    }

    
    for (int i = 1; i<=1000; i++) {        
        if (K[i] >=270) {
            cout << i << endl;
            return 0;
        }
    }
    for (int i = 1; i<=1000; i++) {
        if (K2[i] >=26) {
            cout << i << endl;
            return 0;
        }
    }
    cout << "Obama" << endl;
    
    return 0;
}
