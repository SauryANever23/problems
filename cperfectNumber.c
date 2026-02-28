#include <stdio.h> 
#include <stdlib.h> 
#include <time.h> 

typedef enum {
  false,
  true
}
boolean;

boolean is_perfect(int n)
{
  int sum = 0; 
  for (int i = 1; i < n; i++)
  {
    if (n % i == 0)
    {
      sum += i;
    }
  }
  
  return (sum == n);
}

int main(int argc, char **argv)
{
  int range = atoi(argv[1]);
  clock_t start = clock();
  for (int i = 1; i <= range; i++)
  {
    if (is_perfect(i))
    {
      printf("%d\n", i);
    }
  }
  clock_t end = clock();

  double time_spent = (double) end - start/ CLOCKS_PER_SEC; 

  printf("TIme Spent: %f seconds\n", time_spent);

  return 0;
}
