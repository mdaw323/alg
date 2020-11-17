#include<iostream>
#include<bitset>

using namespace std;

int main() {

    cout << (1<<1) <<endl;
    while(true) {
        int16_t x;
        cin >> x;
        bitset<16> b(x);

        cout << b << endl;

    }
}
