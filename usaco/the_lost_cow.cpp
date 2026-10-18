/* problem: 
 * date: 
 *
 *
 * -1-2-3-4-5-6-7-8-9-10
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
int solve() 
{
  int x, y; cin >> x >> y; 
  int dis = 0; 
  if (x == y) return 0; 
  int i = 0; 
  while (true)
  {
    int pos = x + pow(-1, i)*pow(2, i); 
    if (x < y)
    {
      if (pos - y < 0)
      {
        dis += pow(2, i+1);  
      } else {
        dis += abs(x-y); 
        return dis; 
      }
    }
    else 
    {
      if (y - pos < 0)
      {
        dis += pow(2, i+1);  
      } else {
        dis += abs(x-y); 
        return dis; 
      }
    }
    i++; 
  }

}

int main() {
    // Optimize standard I/O operations for performance
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t = 1;
    
    while (t--) {
        cout << solve() << endl;;
    }
    
    return 0;
}


