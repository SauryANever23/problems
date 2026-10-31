#include <bits/stdc++.h>
using namespace std;

// Type Aliases for faster typing
using ll = long long;

void solve() {
  int n; 
  long long k; 
  cin >> n >> k; 
  vector<ll> a(n); 

  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
  }
  
  ll min = *min_element(a.begin(), a.end());
  ll max = *max_element(a.begin(), a.end());

  if (abs(abs(max-min)-k) <= k)
  {
    cout << (min + k) << "\n"; 
  }
  else 
  {
    cout << -1 << endl;
  }
  
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t = 1;
    cin >> t; // Comment this out if the problem has only 1 test case
    
    while (t--) {
        solve();
    }
    
    return 0;
}


