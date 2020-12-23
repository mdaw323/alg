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

template<class A, class B> ostream& operator <<(ostream& out, const pair<A, B> &p) {
	return out << "(" << p.x << ", " << p.y << ")";
}
template<class A> ostream& operator <<(ostream& out, const vector<A> &v) {
	out << "[";
	FOR(i, 0, v.size()) {
		if(i) out << ", ";
		out << v[i];
	}
	return out << "]";
}


void solve(int tt) {
    DEBUG("solve " + to_string(tt));
    int x, n;
    cin >> n >> x;
    vi a(n+1), s(n);
    for (auto& i : a)
        cin >> i;
    VALUE(a);
    a[n] = x;
    //copy(ALL(a), s.begin());
    //SORT(s);
    vvi dp(n+1, vi(n+1, 0));
    // dp[i][j] miminalna liczba operacji wektora i..n, dla x = a[j]
    int ans = 0;

    for (int i = n; i>=0; i--) {
        FOR (j,0,n+1) {
            x = a[j];

            //dp[i][j] =
        }
    }
    

    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("d.in", "r", stdin);
    // freopen("d.res", "w", stdout);
    int t;
    cin >> t;
    while (t--) {
        solve(t);
    }
}
