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
  // tuu main zakr zo biraad me kahinn dooor se jaise k tim ne bulaya hai jjan 
  int n, m; 
  cin >> n >> m; 
  vector<int> limit(100), bessie(100);
  int pos = 0; 
  for (int i =0; i < n; i++)
  {
    int lenght, speed; 
    cin >> lenght >> speed;
    for (int j = pos; j < lenght + pos; j++)
    {
      limit[j] = speed;
    }
    pos += lenght;
  }
  pos = 0;
  for (int i = 0; i < m; i++)
  {
    int lenght, speed; 
    cin >> lenght >> speed; 
    for (int j = pos; j < lenght + pos; j++)
    {
      bessie[j] = speed; 
    }
    pos += lenght; 
  }

  int max_over = 0; 
  for (int i =0; i < 100; i++)
  {
    max_over = max(max_over, bessie[i] - limit[i]);
  }

  cout << max_over << "\n";
}

int main() {
    // Optimize standard I/O operations for performance
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t = 1;
    
    while (t--) {
        solve();
    }
    
    return 0;
}


