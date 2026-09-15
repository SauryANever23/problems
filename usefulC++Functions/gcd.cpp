#include <iostream> 

// Function to calculate GCD using the Euclidean algorithm
int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

int main()
{
  return 0; 
}
