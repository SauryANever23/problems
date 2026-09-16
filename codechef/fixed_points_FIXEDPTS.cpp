#include <bits/stdc++.h>
using namespace std;

bool check(int n, int k) 
{
    if (n == 1 && k == 0 || n == 2 && k == 1) {
        return false;
    }
    
    // focus on the index, can we match that? 
    
    if (n == k) {
        return true; 
    }
    
    // 1 2 3   3 2 1   1 3 2   3 1 2   2 3 1 
    if (k == n-1) {
        return false; 
    }
    
    if (k == 0)
    {
        return true; 
    }
    
    return true; 
}

int main() {
	// your code goes here
    long t; 
    cin >> t; 
    while (t--)
    {
        int n, k; 
        cin >> n >> k; 
        if (check(n, k)) cout << "Yes" << "\n";
        else cout << "No\n"; 
    }
}

