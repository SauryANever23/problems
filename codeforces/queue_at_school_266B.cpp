/* problem: 
 * date: 
 */
#include <bits/stdc++.h>
using namespace std;

// Type Aliases for faster typing
using ll = long long;
using lli = long long int;
using ld = long double;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vll = vector<ll>;

// Shortcuts for Containers & Loops
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz(a) int((a).size())

// Repetitive Loop Macros
#define rep(i, a, b) for (int i = a; i < b; ++i)
#define per(i, a, b) for (int i = a; i >= b; --i)

// Constants
const int INF = 1e9 + 7;
const ll LINF = 1e18 + 7;
const int MOD = 1e9 + 7; // or 998244353

// Core logic for a single testcase
void solve(int n, int t, string s) {
  // Write your problem logic here
  string ans = s; 
  for (int k =0; k < t; k++)
  {
    vector<int> bpos;
    for (int i = 0; i < n-1; i++)
    {
      if (ans.at(i) == 'B' && ans.at(i+1) == 'G')
      {
        bpos.push_back(i);
      }
    }
    for (auto x: bpos){
      swap(ans[x], ans[x+1]);
    }
  }
  cout << ans << "\n";
}

int main() {
    // Optimize standard I/O operations for performance
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, t; 
    string s; 
    cin >> n >> t; 
    cin >> s; 
    solve(n, t, s);
    return 0;
}


