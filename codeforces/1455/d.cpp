#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<int, int> pi;
typedef vector<pi> vpi;
double EPS = 1e-9;
int INF = 1000000005;
long long INFL = 1000000000000000005LL;
double PI = acos(-1);
int dirx[8] = {-1, 0, 0, 1, -1, -1, 1, 1};
int diry[8] = {0, 1, -1, 0, -1, 1, -1, 1};
#define FOR(a, b, c) for (int a = b; a < c; ++a)
#define SORT(v) sort(v.begin(), v.end())
#define REVERSE(v) reverse(v.begin(), v.end())
#define VALUE(x) cerr << #x << " = " << x << endl
#define DEBUG(x) cerr << x << endl
#define DEBUG_V(a) for_each(ALL(a), [&](auto v) { VALUE(v); })
#define ALL(v) v.begin(), v.end()

void solve() {
    DEBUG("solve");
    int x, n;
    cin >> n >> x;
    vi a(n), s(n);
    for (auto& i : a)
        cin >> i;
    copy(ALL(a), s.begin());
    SORT(s);

    int ans = 0;
    int i = 0;
    for (i = 0; i < n; i++) {
        if (s[i] < x && s[i] < a[i]) {
            ans = -INF;
        }
        if (a[i] < x && s[i] > a[i]) {
            ans++;
        }
    }
    if (ans < 0) {
        ans = -1;
    } else if (ans > 0) {
        // ans++;
    }
    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
