#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

template <int _MOD>
struct ModInt {
    int value;
    static constexpr int MOD = _MOD;

    ModInt(long long v = 0) {
        value = v % MOD;
        if (value < 0) value += MOD;
    }

    ModInt& operator+=(ModInt const& b) {
        value += b.value;
        if (value >= MOD) value -= MOD;
        return *this;
    }
    ModInt& operator-=(ModInt const& b) {
        value -= b.value;
        if (value < 0) value += MOD;
        return *this;
    }
    ModInt& operator*=(ModInt const& b) {
        value = (long long)value * b.value % MOD;
        return *this;
    }

    friend ModInt pow(ModInt a, long long e) {
        ModInt res = 1;
        while (e) {
            if (e & 1) res *= a;
            a *= a;
            e >>= 1;
        }
        return res;
    }
    friend ModInt inv(ModInt a) { return pow(a, MOD - 2); }

    ModInt& operator/=(ModInt const& b) { return *this *= inv(b); }
    friend ModInt operator+(ModInt a, ModInt const b) { return a += b; }
    friend ModInt operator-(ModInt a, ModInt const b) { return a -= b; }
    friend ModInt operator-(ModInt const a) { return 0 - a; }
    friend ModInt operator*(ModInt a, ModInt const b) { return a *= b; }
    friend ModInt operator/(ModInt a, ModInt const b) { return a /= b; }
    friend std::ostream& operator<<(std::ostream& os, ModInt const& a) { return os << a.value; }
    friend bool operator==(ModInt const& a, ModInt const& b) { return a.value == b.value; }
    friend bool operator!=(ModInt const& a, ModInt const& b) { return a.value != b.value; }
};

using mint = ModInt<19>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout << pow(mint(3), 12315) << " " << inv(mint(3)) << " " << mint(3).MOD << endl;
}
