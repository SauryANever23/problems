#include <stdio.h>

void build(int height)
{
  for (int i = 0; i < height; i++)
  {
    for (int j = 0; j < i; j++)
    {
      printf("#");
    }
    printf("\n");
  }
}

int main(void)
{
  int height;
  printf("Enter the desired height: ");
  scanf("%d", &height);

  build(height);

  return 0;
}
