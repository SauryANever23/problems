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
void solve(long k) {
    // we have a k*k chessboard 
    // in how many ways can we add two knighes such that they do not attack eah other 
    // just keep track of position of one knighr
    // for every coordinate in teh k*k space, and every coordinate, it is not attacking, we add to the ans 
    // now how do we figure out the mathematical formula for couting the number of squares, it is attackign based on position 
    // lets create an imaginary attack radius around the knight 
    // in ideal situation, a knight targets 8 squares 
    // so in every co-ordiate, just check how many suares are being blocked 
    // and the suares left are added to the anwer 
    //
    // SO how do we check which squares are blocked 
    // check for border: if in the border, subtracte the left most elemtns, 
    //
    // or maybe just check if a wall is interfereing?? 
    
    // long long ans; 
    //
    // long tot = k*k; 
    //
    // for (int i = 1; i<=k;i++)
    // {
    //   for (int j = 1; j<=k; j++)
    //   {
    //     vector<bool> blocks(4);
    //     if ((k-j)<=1)
    //     {
    //       blocks[0] = true;
    //     }
    //     if ((j-1)<= 1)
    //     {
    //       blocks[1] = true; 
    //     }
    //     if (i - 1 <= 1)
    //     {
    //       blocks[2] = true;
    //     }
    //     if (k-1 <= 1)
    //     {
    //       blocks[3] = true; 
    //     }
    //
    //     ans += tot - (8 - count(blocks.begin(), blocks.end(), true));
    //   }
    // }
    //
 
    // try deriving a genral mathematical formula 
    //
}

int main() {
    // Optimize standard I/O operations for performance
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long t = 1;
    cin >> t; // Comment this out if the problem has only 1 test case
    
    for (long k = 1; k <= t; k++)
    {
      solve(k);
    }
    return 0;
}


