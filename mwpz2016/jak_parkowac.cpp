#include <iostream>
#include <unordered_map>
#include <vector>
#include <math.h>
#include <set>
#include <algorithm>

typedef unsigned long long ull;
const ull MAX_K = 1e18;
const ull MOD = 1e9 + 7;
using namespace std;

int unknownDivisor = MAX_K + 1;

set<ull> primes;

bool miller_rabin_prime_check(ull x, ull n) {
    if (x>=n) return 0;
    ull d = 1, y;
    int t= 0, l= n-1;
    while (!(l & 1)) {
        ++t;
        l >>= 1;
    }
    for (; l>0 || t--; l>>=1) {
        if (l & 1) d= (d*x) %n;
        if (!l) {
            x = d;
            l = -1;
        }
        y = (x*x) % n;
        if (y == 1 && x != 1 && x != n-1) return 1;
        x = y;
    }
    return x != 1;
}


bool is_prime(ull x) {    
    return !(x<2 
        || miller_rabin_prime_check(2,x) 
        || miller_rabin_prime_check(3,x) 
        || miller_rabin_prime_check(5,x) 
        || miller_rabin_prime_check(7,x)
        || miller_rabin_prime_check(11,x)
        || miller_rabin_prime_check(13,x)
        || miller_rabin_prime_check(17,x)
        || miller_rabin_prime_check(19,x)
        || miller_rabin_prime_check(23,x)
        );
        
}

void gen_primes() {
    primes.insert(2);
    for (ull i = 3; i < 1e6; i+=2) {
        if (is_prime (i)) primes.insert(i);
    }

}

ull find_max_prime(ull x) {   
    ull t = x, m = 1;
    for (auto &d : primes) {
        if (d * d > t) break;
        while ( t % d == 0 && t > 1) {
            m = d;
            t /= d;               
        }            
    }
    if (is_prime(t)) return max(m,t);
}

vector<ull> find_divisors(ull x) {
    //set<ull> r;
    vector<ull> res;
    ull t = x;
    res.push_back(1);
    for (auto &d : primes) {
        if (d > t) break;
        ull acc = 1;
        auto sz = res.size();
        while ( t % d == 0 && t > 1) {
            acc *= d;
            for (int i = 0; i<sz; i++)
                res.push_back(acc * res[i]);                        
            t /= d;               
        }            
    }
    if (is_prime(t)) {  
        cout << t << " prime\n";
        auto sz = res.size();
        for (int i = 0; i<sz; i++)
            res.push_back(t * res[i]); 
    } else {
        ull s = sqrt(t);        
        if (t > 1 && t == s * s) {
            cout << t << " " <<s<<" sqrt\n";
            auto sz = res.size();
            for (int i = 0; i<sz; i++) {
                res.push_back(s * res[i]); 
                res.push_back(t * res[i]); 
            }
        } else if (t > 1) {
            cout << t << " unknown\n";
            auto sz = res.size();
            for (int i = 0; i<sz; i++) {
                res.push_back(unknownDivisor++);
                res.push_back(unknownDivisor++);
                res.push_back(t * res[i]);
            }
        }
    }
    //for ( auto &i : res )
    //    r.insert(i);
        
    sort(res.begin(), res.end());
    cout << "size : " << res.size() << endl;
    return res;
}

ull gcd(ull a, ull b) {
    return b == 0 ? a : gcd(b, a % b);
}


int main () {
    
    int n;
    ull k[7];
    cin >> n;
    for (int i = 0 ; i<n; i++) {
        cin >> k[i];
    }
    
    vector<ull> divisors[7];
    set<ull> merged_divisors;
    gen_primes();
    
    for (int i = 0; i< n-1; i++) 
        for (int j = i+1; j<n; j++) {
            auto g = gcd(k[i], k[j]);
            if (g > 1) {
                auto gg = find_max_prime(g);
                if (gg > 1e6)
                    primes.insert(gg);
            }
            
        }
    //cout << primes.size();
    //find_divisors(99999989);
    //auto g = gcd(99999989*2, 99999989*4);
    for (int i = 0; i< n ; i++) {
        divisors[i] = find_divisors(k[i]);
        for ( auto &e : divisors[i]) 
            merged_divisors.insert(e);
    }
    
     
    //find_divisors(99999989*99999989, 1);
    //find_divisors(99999989*99999959);
    vector <ull> res[7];    
    ull sum = 0;
    for (auto &e : merged_divisors) {
        cout << e << "\t";
    }
    cout <<endl;
    for (auto &e : merged_divisors) {
        if (binary_search(divisors[0].begin(), divisors[0].end(), e)) {
            res[0].push_back(1);
            sum++;
        } else {
            res[0].push_back(0);
        }
    }
    for (auto &e : res[0]) {
        cout << e << "\t";
    }
    cout << " sum: " << sum << endl;
    for (int i = 1; i<n; i++) {
        int d = 0;
        for (auto &e : merged_divisors) {
            if (binary_search(divisors[i].begin(), divisors[i].end(), e)) {
                res[i].push_back(sum % MOD);                
                for (int j = i-1 ; j >=0; j--) {
                    res[i][d] = (MOD + res[i][d] - res[j][d]) % MOD;
                }
            } else {
                
                res[i].push_back(0);
            }
            d++;
            cout << res[i][d-1] << "\t";
        }
        sum = 0;
        for (auto &e : res[i]) {
            sum = (sum + e) % MOD;
        }
        cout << " sum: " << sum << endl;
    }
    
    
    
    for (auto &i : merged_divisors) {
        cout << i << "\t";
    }
    cout << sum;
    
// 2 1914793758 123456789012345678
// 2 2362855497372 123456789012345678

    
//  99999989
//  99999971 * 99999989
//  99999959
    return 0;

}