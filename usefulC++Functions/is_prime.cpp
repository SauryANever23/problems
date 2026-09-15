#include <iostream> 

bool isPrime(int n) {
    // 1. Base cases: numbers less than or equal to 1 are not prime
    if (n <= 1) return false;
    
    // 2. 2 and 3 are prime
    if (n <= 3) return true;
    
    // 3. Exclude all remaining even numbers and multiples of 3
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    // 4. Check factors from 5 up to sqrt(n)
    // We increment by 6 to skip even numbers and multiples of 3 (checking i and i + 2)
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false; // Found a factor, so n is not prime
        }
    }
    
    return true; // No factors found, n is prime
}

int main()
{
  return 0;
}
