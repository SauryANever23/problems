/* problem: 
 * date: 
 */
#include <iostream> 
#include <utility>
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
      
}

void BubbleSort(int arr[], int n)
{
  // n is the size of array 
  // O(n^2) time   
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n-1; j++)
    {
      // check the order of the elemnts and swap them if necessary 
      if (arr[j] > arr[j+1])
      {
        swap(arr[j], arr[j+1]);
      }
    }
  }
}

int main() {
    // Optimize standard I/O operations for performance
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    //
    // int t = 1;
    // cin >> t; // Comment this out if the problem has only 1 test case
    //
    // while (t--) {
    //     solve();
    // }
    //
    
    int arr[10] = {3, 5, 12, 99, 6, 13, 90, 35, 23, 48};
    int n = 10; 
    for (int x : arr){
      cout << x << " ";
    }
    cout << endl; 
    BubbleSort(arr, n); 
    for (int x : arr)
    {
      cout << x << " ";
    }
    cout << endl; 
    return 0;
}


