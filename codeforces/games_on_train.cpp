#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <string> 
#include <sstream>

using namespace std;

int findK(vector<int>& vec)
{
  auto max_it = max_element(vec.begin(), vec.end());
  int max_val = *max_it; 
  int val_k;
  vector<int> possible_k; 

  for (int i = 0; i < vec.size(); i++)
  {
    val_k = max_val - vec[i]; 
    possible_k.push_back(val_k+1);
  }

  auto max_k = max_element(possible_k.begin(), possible_k.end());

  return *max_k;
}

int main(void)
{
  int t,n; 
  cin >> t; 
  vector<int> soln;
  for (int i = 0; i < t; i++)
  {
    cin >> n;
    cin.ignore();
    string line; 
    getline(cin, line); 
    stringstream stream(line);
    vector<int> numbers; 
    int temp; 
    
    while (stream >> temp)
    {
      numbers.push_back(temp);
    }

    soln.push_back(findK(numbers));

  }

  for (int val : soln) cout << val << endl;  
  return 0;

}
