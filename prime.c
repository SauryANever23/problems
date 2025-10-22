#include <stdio.h>
#include <stdlib.h>

int isprime(int num)
{
  int count = 0;
  for (int i = 1; i <= num; i++)
  {
    if (num % i == 0)
    {
      count++;
    }
  }
  
  if (count == 2)
  {
    return 1;
  }
  return 0;
}

int main(int argc, char *argv[])
{
  int n = atoi(argv[1]);
  
  printf("isprime: %d", isprime(n));

  return 0;
}
