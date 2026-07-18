#include <iostream>

using namespace std; 

int main()
{
  ios::sync_with_stdio(0);
	cin.tie(0);

  int h, w; 
  
  cin >> h >> w;
  float H = h / 100.0f; 
  
  float bmi = w / (H * H); 

  if (bmi >= 25)
  {
    cout << "Yes" << "\n";
  }
  else 
  {
    cout << "No" << "\n";
  }
}
