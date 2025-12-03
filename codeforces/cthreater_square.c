#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  long long m,n,a;
  scanf("%lld %lld %lld", &m, &n, &a);
  long long lenght = (m+a-1)/a; 
  long long width = (n+a-1)/a;

  long long total = lenght * width;
  printf("%lld\n", total);

  return 0;
}
