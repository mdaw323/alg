#include <bits/stdc++.h>
using namespace std;

#define debug(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); err(_it, args); }
void err(istream_iterator<string> it) {}
template<typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args) {
    cerr << "["<< *it << " = " << a << "]"<< endl;
    err(++it, args...);
}
using ll = long long;

int divisors(ll n) {
    int d =0;
    for (ll i = 1; i <=n; i++) {
        if (n % i ==0) {
            d++; 
        }
    }
    return d;
}

ll primes[100];
vector<pair<ll, int>> ap;
const ll MN = 2000000000;

void gen() {
    vector<int> L = {15,10,5,3,2,1,1,1,1,1};
    vector<int> V = {-1 ,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    int s = L.size();
    int i = 0;

    while (i < s) {
        i = 0;
        V[i]++;
        bool wyrownaj = false;
        while (V[i] > L[i] && i < s) {
            wyrownaj = true;
            V[++i]++;
        }
        if (wyrownaj) {
            for (int j = 0; j < i; j++) {
                V[j] = V[i];
            }
        }
        
        int cnt = 1;
        ll c = 1;
        bool za_duza= false;
        for (int j =0; j < s && V[j] != 0; j++) {
            cnt *= V[j] +1;
            for (int k = 0; k < V[j]; k++) {
                c *= primes[j];
                if (c>MN) {
                    za_duza = true;
                    break;
                }
            }
            if (za_duza) {
                break;
            }
        }
        if (!za_duza) {
            ap.emplace_back(make_pair(c, cnt));
            //cout << c << " " << cnt << endl;
        }


    }

}

void findPrimes(int n) {
    int k = 5;
    int p = 13;
    primes[0] = 2;
    primes[1] = 3;
    primes[2] = 5;
    primes[3] = 7;
    primes[4] = 11;
    while (k < n) {
        bool prime = true;
        for (int i = 2; i * i <= p; i+=1) {
            if (p % i == 0) {
                prime = false;
                break;
            }
        }
        if (prime) {
            primes[k++] = p;
        }
        p++;        
    }
}



void fact(ll n) {
    int pi = 0;
    int cnt = 1;
    while (n > 1) {
        ll p = primes[pi];
        int cp = 0;
        while (n % p == 0) {
            n /= p;
            cp++;
        }
        cnt *= cp+1;
        cout << p<< "^" << cp << " ";
        pi++;
    }
    cout <<" ----> " <<cnt << endl;
}

int main() {
    ios::sync_with_stdio(false);
    ll n;
    cin >> n;
    findPrimes(100);
    gen();
    sort(ap.begin(), ap.end());
    int maxv = 0;
    ll liczba;
    ll ans = 1;
    int v;
    vector<ll> antypierwsza;
    for (auto &a : ap) {
        tie(liczba,v) = a;
        if (maxv < v) {
            if (liczba <=n) {
                ans = liczba;
            }
            antypierwsza.emplace_back(liczba);
            maxv = v;
        }
    }
    
    cout << ans << endl;

    
}
