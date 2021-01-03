#include <algorithm>
#include <cmath>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
//#define double long long;
typedef long double ld;
#define double long double
const double e = 0.00000005;
const double pi = 3.1415926535898;
inline int getint() {
    int val = 0;
    char c;
    while ((c = getchar()) && !(c >= '0' && c <= '9'))
        ;
    do {
        val = (val * 10) + c - '0';
    } while ((c = getchar()) && (c >= '0' && c <= '9'));
    return val;
}
const long long INF = 100000000000000;
const int Y = 1000000;
int gcd(int i, int j) {
    if (j == 0)
        return i;
    else
        return gcd(j, i % j);
}
const long long m = 1000000009;
int arr[20];
int ost[21];
int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false);
    // freopen("INPUT.TXT", "r", stdin);
    //freopen("OUTPUT.TXT", "w", stdout);
    int n, w;
    cin >> n >> w;
    for (int i = 0; i < n; ++i) cin >> arr[i];
    int res = 21;
    while (true) {
        if (1.0 * clock() / CLOCKS_PER_SEC > 0.15) break;
        random_shuffle(arr, arr + n);
        int ct = 1;
        int nr = 0;
        for (int i = 0; i < n; ++i) {
            nr += arr[i];
            if (nr > w) {
                bool fal = false;
                for (int j = 1; j < ct; ++j) {
                    if (arr[i] <= ost[j]) {
                        ost[j] -= arr[i];
                        fal = true;
                        break;
                    }
                }
                if (fal) {
                    nr -= arr[i];
                } else {
                    ost[ct] = (w - (nr - arr[i]));
                    nr = arr[i];
                    ++ct;
                }
            }
        }
        res = min(res, ct);
    }
    cout << res;
    return 0;
}
/* Wed Apr 01 2020 21:05:33 GMT+0300 (MSK) */
