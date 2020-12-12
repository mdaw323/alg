#include <bits/stdc++.h>
using ll = long long;
using namespace std;

int main() {
    int t;
    ll n;

    vector<ll> primes = {2, 3, 5, 7};

    for (ll i = 11; i <= 103000; i += 2) {
        ll j = 0;
        bool is_prime = true;
        while (primes[j] * primes[j] <= i) {
            if (i % primes[j] == 0) {
                is_prime = false;
                break;
            }
            j++;
        }
        if (is_prime) {
            primes.push_back(i);
        }
    }

    cin >> t;
    while (t--) {
        cin >> n;
        ll nn = n;
        vector<pair<ll, ll>> f;
        ll j = 0;
        while (n > 1 && primes[j] * primes[j] <= n) {
            ll c = 0;
            while (n % primes[j] == 0) {
                c++;
                n = n / primes[j];
            }
            if (c > 0) {
                f.push_back({c, primes[j]});
            }
            j++;
        }
        if (n > 1) {
            f.push_back({1, n});
        }

        sort(f.rbegin(), f.rend());
        for (ll i = 0; i < f.size(); i++) {
            // cout << f[i].first << ":" << f[i].second << " ";
        }

        if (f.size() > 0 && f[0].first > 1) {
            cout << f[0].first << endl;
            ll last = f[0].second;
            for (ll i = 0; i < f[0].first - 1; i++) {
                cout << last << " ";
            }
            for (ll i = 1; i < f.size(); i++) {
                for (ll j = 0; j < f[i].first; j++) {
                    last *= f[i].second;
                }
            }
            cout << last << endl;

        } else {
            cout << 1 << endl;
            cout << nn << endl;
        }
    }
}
