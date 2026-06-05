#include <iostream> 
#include <vector> 

using namespace std; 

vector<int> TwoSum(vector<int>& nums, int target)
{
  vector<int> vec; 
  
  for (int i = 0; i < nums.size(); i++)
  {
    for (int j = 0; j< nums.size(); j++)
    {
      if (i != j && nums.at(i) + nums.at(j) == target)
      {
        vec.push_back(i);
        vec.push_back(j);
        return vec;
      }
    }
  }

  return vec; 
}

int main(void)
{
  vector<int> list = {2, 7, 11, 15};
  int target = 9;

  vector<int> output = TwoSum(list, target);
  for (int vals: output)
  {
    cout << vals << " ";
  }
}
