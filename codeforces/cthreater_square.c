#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int m,n,a;
  scanf("%d %d %d", &m, &n, &a);
  int lenght = (m+a-1)/a; 
  int width = (n+a-1)/a;

  int total = lenght * width;
  printf("%d", total);

  return 0;
}
