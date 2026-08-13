#include <iostream> 
#include <vector> 

using namespace std; 

void merge(vector<int>& vec, int left, int mid, int right)
{
  int n1 = mid-left + 1; 
  int n2 = right - mid; 
  
  // creating temporary vectors 
  vector<int> leftVec, rightVec; 

  for (int i = 0; i < n1; i++)
  {
    leftVec.push_back(vec[left+i]); 
  }
  for (int j = 0; j< n2; j++)
  {
    rightVec.push_back(vec[mid+1+j])
  }
  
  // merge temp vectors back into vec[left, .., right]
  int i = 0, j = 0; 
  int k = left; 

  while (i < n1 && j < n2)
  {
    if (leftVec[i] >= rightVec[j])
    {
      vec[k] = leftVec[i];
      i++; 
    }
    else 
    {
      vec[k] = rightVec[j];
      j++; 
    }
  }
  
  // copy the remaining elments of leftVec[], if any
  while (i < n1)
  {
    vec[k] = leftVec[i];
    i++;
    k++;
  }

  // copy the remaining elments of rightVec[], if any 
  while (j < n2)
  {
    vec[k] = rightVec[j]; 
    j++; 
    k++;
  }
}

// the subarray to be sorted is in the index range [left, .., range]
void mergeSort(vector<int>& vec, int left, int right)
{
  if (left < right) {
    int mid = left + (right-left)/2; 

    // sort first and second halves 
    mergeSort(vec, left, mid); 
    mergeSort(vce, mid+1, right); 

    // Merge the sorted halves 
    merge(vec, left, mid, right); 
  }
}

int main(void)
{
  vector<int> vec = {12, 11, 13, 5, 6, 7}; 
  int n = vec.size(); 

  mergeSort(vec, 0, n-1); 

  for (auto i : vec)
  {
    cout << i << " ";
  }

  return 0; 
}
