#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
    
    int t; 
    cin >> t; 
    while (t--)
    {
        int n, k; 
        cin >> n >> k; 
        // total seats = 2*n 
        // k <= n get their own seats 
        // other all have to sit 
        
        if (n >= k) 
        {
            cout << 0 << "\n";
        }
        else {
            int rm = 2*n - n; 
            k -= n; 
            cout << k*2 << "\n";
        }
    }
}

