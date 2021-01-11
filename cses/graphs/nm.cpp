#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <string>
#include <cmath>
#include <numeric>


using namespace std;
//Macros
#define  ll      int
#define  endl    "\n"
#define  fastIO  ios_base::sync_with_stdio(false);cin.tie(NULL);
#define  pb push_back
#define pll pair<ll,ll>
#define F first
#define S second


const ll nodes = 2e5 + 10;
vector <ll> adj[nodes];
vector <ll> parent(nodes);
vector <ll> visited(nodes);
vector <pair <ll,ll>> moves={{1,0},{-1,0},{0,1},{0,-1}};
string dirs = "DURL";
vector <string> grid(1009);
vector <vector<ll>> visitedG(1009,vector<ll>(1009,0));
vector <ll> color(nodes);


bool flag = 1;
vector <ll> ans;
vector <ll> tmp;
ll nd;

void dfs(ll node,ll p){
    if(flag==0) return;
    visited[node]= 1;
    for(ll x: adj[node]){
        if(x == p)
            continue;
        if(!visited[x] && flag) {
            parent[x] =  node;
            dfs(x, node);
        }
        else if(flag){
            flag = 0;
            parent[x] = node;
            nd = node;
            return;
        }
    }
}



void  addEdge(ll x,ll y){
    adj[x].push_back(y);
    adj[y].push_back(x);
}

void solve(){
    ll n,m;
    cin>>n>>m;
    for(ll i=0;i<m;i++){
        ll x,y;
        cin>>x>>y;
        addEdge(x,y);
    }

    for(ll i =  1;i<=n;i++)
    {
        if(!flag) break;
        if(visited[i]==false){
            color[i] = 1;
            dfs(i,-1);
        }
    }

    if(flag){
        cout<<"IMPOSSIBLE";
    }
    else {
        vector <ll> ans ={nd};
        ll cur = nd;
        while(parent[cur] != nd){
            cur = parent[cur];
            ans.push_back(cur);
        }
        ans.push_back(nd);
        cout<<ans.size()<<endl;
        for(ll x:ans)cout<<x<<" ";
    }
}



#define  isTestCases 0


int main(){
    fastIO
    ll t=1;
#if isTestCases
    cin>>t;
#endif
    while(t--) {
        solve();
    }
    return 0;
}
