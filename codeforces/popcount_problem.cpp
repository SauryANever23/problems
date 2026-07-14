#include <iostream>
#include <vector> 
#include <bit> 

using namespace std; 

int main(void)
{
  int t, n, k; 
  
  cin >> t; 
  vector<int> soln;
  for (int i = 0; i < t; i++)
  {
    cin >> n >> k; 

    int total = 0; 

    size_t N = n / k;
    if (k > n)
    {
      total += n; 
    }
    else 
    {
      for (int j = 0; j < k; j++)
      {
        total += popcount(N);
      }
    }
    soln.push_back(total);
    
  }

  for (int sol : soln)
  {
    cout << sol << endl;
  }

  return 0;
}
