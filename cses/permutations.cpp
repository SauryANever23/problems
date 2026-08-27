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
void solve() {
    // for n, 
    // take the odd numbers and the even numebrs, 
    // n = 4. 1 3  2 
    // fist print the odd numebr then the even numebrs 
    long long n; cin >> n; 
    if (n <= 3 && n > 1)
    {
      cout << "NO SOLUTION" << "\n";
    }
    else if (n == 4)
    {
      vector<int> v = {2, 4, 1, 3};
      for (int x: v)
      {
        cout << x << " ";

      }
      cout << "\n";
    }
    else {
      vector<ll> odd;
      vector<ll> even; 
      for (int i = 1; i <= n; i++)
      {
        if (i%2==0) even.push_back(i);
        else odd.push_back(i);
      }
      for (long long x: odd)
      {
        cout << x << " ";
      }
      for (long long x: even)
      {
        cout << x << " ";
      }
      cout << "\n";
    }
}
 
int main() {
    // Optimize standard I/O operations for performance
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t = 1;
    // cin >> t; // Comment this out if the problem has only 1 test case
    
    while (t--) {
        solve();
    }
    
    return 0;
}
 

