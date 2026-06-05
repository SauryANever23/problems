#include <iostream> 
#include <cmath>

using namespace std; 

class Solution {
public:
    bool isPalindrome(int x) {
        int rev_x = 0; 
        int val = x;
        while (x != 0)
        {
            rev_x = rev_x*10 + x % 10;
            x = x / 10; 
  
        }
        if (rev_x == val)
        {
            return true;
        }
        else {
            return false;
        }
    }
};

int main(void)
{
  Solution sol; 
  cout << sol.isPalindrome(121) << endl; 

}
