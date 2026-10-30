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
  vector<string> target(10); 
  for (int i =0; i < 10; i++)
  {
    string s; 
    cin >> s; 
    target[i] = s; 
  }
  int points = 0; 
  vector<int> shots(5, 0);
  for (int i =0; i < 5; i++)
  {
    string s1 = target[i].substr(i+1, 9-i+1); 
    string s2 = target[9-i].substr(i+1, 9-i+1); 
    int sm = count(s1.begin(), s1.end(), 'X');
    sm += count(s1.begin(), s1.end(), 'X');
    shots[i] += sm; 
  }

  for (int i =0; i < 10; i++)
  {
    int cnt = 0; 
    if (target[i].at(0) == 'X')
    {
      cnt++;
    } else if (target[i].at(9) == 'X')
    {
      cnt++;
    }
    shots[0] += cnt; 
  }

  for (int i = 1; i <= 9; i++)
  {
    int cnt = 0; 
    if (target[i].at(1) == 'X')
    {
      cnt++; 
    } 
    if (target[i].at(9) == 'X')
    {
      cnt++;
    }
    shots[1] += cnt; 
  }

  for (int i = 1; i <= 8; i++)
  {
    int cnt =0; 
    if (target[i].at(2) == 'X')
    {
      cnt++;
    } if (target[i].at(8) == 'X') cnt++;
    shots[2] += cnt;
  }

  for (int i = 2; i <= 7; i++)
  {
    int cnt =0; 
    if (target[i].at(3) == 'X')
    {
      cnt++;
    }
    if (target[i].at(7) == 'X') cnt++;
    shots[2] += cnt;
  }

  for (int i = 3; i <= 6; i++)
  {
    int cnt = 0; 
    if (target[i].at(3) == 'X') cnt++; 
    if (target[i].at(6) == 'X') cnt++; 
    shots[3] += cnt;
  }

 
  points = 1*shots[0] + 2*shots[1] + 3*shots[2] + 4*shots[3] + 5*shots[4]; 
  cout << points << "\n";
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


