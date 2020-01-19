#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const ll M = 4*1e16;

struct Point {
    ll x,y;
};

ll dist(Point a, Point b) {
    return abs(b.x - a.x) + abs(b.y - a.y);
}

int main() {
    ios::sync_with_stdio(false);
    ll x,y, ax,bx,ay,by,t;
    cin >> x >> y >> ax >> ay >> bx >> by;
    
    vector<Point> s;
    while (x < M && y < M) {        
        s.emplace_back(Point{x,y});
        x = ax * x + bx;
        y = ay * y + by;
    }

    int maxv = 0;
    cin >> x >> y >> t;
    for (int i = 0 ; i < (int)s.size(); i++) {
        //cerr << s[i].x << " " <<s[i].y << endl;
        Point m = Point{x,y};
        ll d = 0ll;
        int v = 0;
        int j = i;
        while (j >= 0 && d + dist(m,s[j]) <= t) {
            d+= dist(m,s[j]);
            m = s[j];
            v++;
            j--;
        }

        j = i+1;
        while (j < (int)s.size() && d + dist(m,s[j]) <= t) {
            d+= dist(m,s[j]);
            m = s[j];
            v++;
            j++;
        }
        maxv = max(maxv, v);

    }
    cout << maxv << endl;
    
    return 0;
}
