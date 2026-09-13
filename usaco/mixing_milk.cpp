#include <bits/stdc++.h> 

using namespace std; 

using ll = long long; 

int main(void)
{
  // 3 buckets, each bucket, may have idfdernt size and may not be completely filled 
  // milk is transferred from a to b untill a becomes empty or b becomes full 
  // and so b from c in the same way 
  // we have to repreat this process 100 times 
  //
  // input: 
  // 3 liens, c1 and m1, (capacity of bucket and the amount of milk init)
  
  const int n = 3; 

  vector<int> m(n);
  vector<int> c(n);
  
  for (int i = 0; i<n; i++)
  {
    cin >> c[i] >> m[i];
  }

  const int iteration = 100; 

  for (int i = 0; i < 100; i++)
  {
    int b1 = i % n; 
    int b2 = (i+1) % n; 
    
    int amt = min(m[b1], c[b2]-m[b2]);

    m[b2] += amt; 
    m[b1] -= amt;
  }
  
  for (auto x: m) cout << x << " ";
  cout << endl;
}
