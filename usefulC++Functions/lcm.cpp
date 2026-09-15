#include <iostream>

// Function to calculate GCD using the Euclidean algorithm
int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

// Function to calculate LCM
int lcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    
    // Dividing 'a' before multiplying prevents potential integer overflow
    return (a / gcd(a, b)) * b; 
}

int main() {
    int num1 = 12, num2 = 18;
    std::cout << "The LCM of " << num1 << " and " << num2 << " is: " << lcm(num1, num2) << std::endl;
    return 0;
}
