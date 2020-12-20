using ll = long long;

int main() {
    ll M = 1e9 + 7;
    ll f1 = 1, f2 = 1;
    for (ll i = 1; i < 10000000000000; i += 2) {
        f1 = (f1 * i) % M;
        f2 = (f2 * (i + 1)) % M;
    }
    ll f = (f1 * f2) % M;
}
