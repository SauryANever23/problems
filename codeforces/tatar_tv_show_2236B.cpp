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
    // Write your problem logic here
    long long n; 
    long long k; 
    string str; 
    cin >> n >> k; 
    cin >> str;
    const int MAXN = 200000;
    bitset<MAXN> s;
    for (int i = 0; i < n; i++) {
        s[i] = str[i] - '0';
    }
    for (long long i = 0; i < n-k; i++)
    {
      if (s[i] && s[i+k])
      {
        s[i] = 0; 
        s[i+k] = 0;
      }
    }
    
    if (s.count() > 0) cout << "NO" << "\n"; 
    else cout << "YES" << "\n";
    
}

int main() {
    // Optimize standard I/O operations for performance
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t = 1;
    cin >> t; // Comment this out if the problem has only 1 test case
    
    while (t--) {
        solve();
    }
    
    return 0;
}


