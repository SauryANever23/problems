#include <stdio.h>

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
  int num;
  printf("give num: ");
  scanf("%d", &num);
  printf("isprime: %d", isprime(num));

  return 0;
}
