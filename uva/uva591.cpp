#include <iostream>
using namespace std;

int main() {
    int n;
    int h[101];
    cin >> n;
    int set = 0;
    while (n != 0) {        
        int s = 0;
        for (int i = 0; i <n ; i++) {
            cin >> h[i];
            s+= h[i];
        }
        int k = s/n;
        s = 0;
        for (int i = 0; i<n; i++) 
            if (h[i] > k) s+=h[i] -k;
        cout << "Set #" << ++set << "\nThe minimum number of moves is "<<s<<".\n\n";
        cin >> n;
    }
}