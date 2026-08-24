/* problem: 
 * date: 
 */
// #include <bits/stdc++.h>
#include <iostream> 
#include <vector> 
#include <algorithm> 
using namespace std;

// Type Aliases for faster typing
// using long long = long long;
// using long longi = long long int;
// using ld = long double;
// using pii = pair<int, int>;
// using plong long = pair<ll, ll>;
// using vi = vector<int>;
// using vlong long = vector<ll>;

// Shortcuts for Containers & Loops
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define along long(v) (v).begin(), (v).end()
#define ralong long(v) (v).rbegin(), (v).rend()
#define sz(a) int((a).size())

// Repetitive Loop Macros
#define rep(i, a, b) for (int i = a; i < b; ++i)
#define per(i, a, b) for (int i = a; i >= b; --i)

// Constants
const int INF = 1e9 + 7;
const long long LINF = 1e18 + 7;
const int MOD = 1e9 + 7; // or 998244353

// Core logic for a single testcase
void solve() {
    // Write your problem logic here
    long long n; 
    // vector<long long> nums; 
    cin >> n; 
    vector<long long> arr(n-1); 
    for (long long &x : arr) cin >> x; 
    
    // sorting the array 
    sort(arr.begin(), arr.end()); 
    bool test= false; 
    for (int i = 0; i < n-1; i++)
    {

      if (arr[i] != i+1)
      {
        cout << i+1 << "\n"; 
        test = true;
        break;
      }
    }

    if (!test)
    {
      cout << n << "\n";
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


