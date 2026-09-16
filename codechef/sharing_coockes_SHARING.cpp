#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
    int a, b; 
    cin >> a >> b; 
    
    if ((a-b) % 2 != 0)
    {
        cout << -1 << "\n";
    } else {
        cout << (int)abs(a-b) / 2 << "\n";
    }
}

