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
// Function to calculate GCD using the Euclidean algorithm
int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

// Function to calculate LCM
int lcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    
    // Dividing 'a' before multiplying prevents potential integer overflow
    return (a / gcd(a, b)) * b; 
}

bool isPrime(int n) {
    // 1. Base cases: numbers less than or equal to 1 are not prime
    if (n <= 1) return false;
    
    // 2. 2 and 3 are prime
    if (n <= 3) return true;
    
    // 3. Exclude all remaining even numbers and multiples of 3
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    // 4. Check factors from 5 up to sqrt(n)
    // We increment by 6 to skip even numbers and multiples of 3 (checking i and i + 2)
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false; // Found a factor, so n is not prime
        }
    }
    
    return true; // No factors found, n is prime
}


void solve() {
    // Write your problem logic here
   string s, t; 
   cin >> s; 
   cin >> t; 
  
   if (s+t != t + s)
   {
      cout << -1 << "\n";
      return;
   }
    
   int res = lcm(s.length(), t.length()); 

   string ans = "";

   for (int i =0; i < res/(int)t.size(); i++)
   {
     ans += t; 
   }

   cout << ans << "\n";
   
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


