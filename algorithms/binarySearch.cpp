#include <iostream> 
#include <vector> 

int binarySearch(vector<int>& vec, int n)
{
  int a =0, b = vec.size()-1;
  while (a <=b)
  {
    int k = (a+b)/2; 
    if (vec[k] == n)
    {
      return k; 
    }
    if (vec[k]>x) b = k-1; 
    else a = k+1
  }
}

int main(void)
{
  vector<int> v = {1, 5, 5, 51, 123, 512, 12, 41, 55}; 
  sort(v.begin(), v.end()); 
  int n; 
  n = 12; 
  cout << binarySearch(v, n) << endl; 

  return 0;
}
