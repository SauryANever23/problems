/* problem: 
 * date: 
 */

/*
 *
 *Try this again, with clear mathematical derivation 
 and come to a more clearner and structured solution 
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
  long long x;
  long long y; 
  cin >> y >> x; 
  if (y==1 && x ==1)
  {
    cout << 1 << "\n";
    return;
  }
  if (y == 1 && x ==2)
  {
    cout << 2 << "\n";
    return; 
  }
  // row - y 
  // basically 
  // the distance from every layer is of n^2 - (n-1)^2 
  // distnace, 
  // here n is the layer? 
  // so how do we fidure otu whic row and column is in which layer? 

  // layer ! rows: 1 -2 column 1-2 
  // layer 2 rows: 1-3, column: 1-3 
  // layer 3 rowsL 1-4, column: 1-4
  // and so on.. 
  //
  // so how we have found the layer, how do we descern the elemnt?? 
  // lets try this, take the max value: 
  // whihc will give the layer, then take the min value, which will give the 
  // value insdie the layer, 
  // now check th emax value for layer 3 
  // whic is 3^2 and coordinate are: 1-3
  // now min value of layer 3 is (3-1)^2 + 1, so coordinate is, 3-1
  // this becomes opposite if the layer is even 
  //
  // so now you calulate the diffet from max positoin
  // like max pos: 1-3 
  // we have 2-3, whic is one down, 
  //
  // now how do we calcualte the positoin differcen? 
  //
  // limit is (layer-1) to (1-layer) 
  // we are given row and column 
  // all pissiton (n,1), (n,2), (n,3), ... (n,n), (n-1, n), (n-2, n)) ..., (1, n)
  // is row is max, then we look at the colum up to n 
  // so we get the genral formula
  
  long long n = max(y, x); 
  long long m = min(y, x); 
  if (n%2==0) {
      if (n==m) 
      {
        cout << ((n*n)+((n-1)*(n-1)+1))/2 << "\n";
        return;
      }
      if (y > x)
      {
        long long pos = x - 1; 
        cout << (n*n)-pos << "\n";
        return;
      }
      else 
      {
        long long pos = y - 1; 
        cout << ((n-1)*(n-1)+1)+pos << "\n"; 
        return;
      }
  } else {
    if (n==m)
    {
      cout << ((n*n)+((n-1)*(n-1)+1))/2 << "\n";
      return;
    }
    if (y>x)
    {
      long long pos = x - 1; 
      cout << ((n-1)*(n-1)+1)+pos << "\n";
      return;
    }
    else 
    {
      long long pos = y -1; 
      cout << (n*n)-pos << "\n";
      return;
    }
      
  }
}

int main() {
    // Optimize standard I/O operations for performance
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long t = 1;
    cin >> t; // Comment this out if the problem has only 1 test case
    
    while (t--) {
        solve();
    }
    
    return 0;
}


