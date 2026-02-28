#include <stdio.h> 
#include <ctype.h> 
#include <stdlib.h> 

bool is_perfect(int n)
{
  int sum = 0; 
  for (int i = 1; i < n; i++)
  {
    if (n % i == 0)
    {
      sum += i;
    }
  }

  if (sum == n)
  {
    return true;
  }
}

int main(int argc, char **argv)
{
  int range = atoi(argv[1]);
  for (int i = 1; i <= range; i++)
  {
    if (is_perfect(i))
    {
      puts(i);
    }
  }
}
