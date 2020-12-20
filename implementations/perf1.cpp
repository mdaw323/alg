using ll = long long;

int main() {
    ll M = 1e9 + 7;
    ll f = 1;
    for (ll i = 1; i < 10000000000000; i++) {
        f = (f * i) % M;
    }
}
