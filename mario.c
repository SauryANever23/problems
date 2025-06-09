#include <stdio.h>

void build(int height)
{
  for (int i = 1; i <= height; i++)
  {
    for (int j = 0; j < i; j++)
    {
      printf("#");
    }
    printf("\n");
  }
}

void revrse_build(int height)
{
  for (int i = 1; i <= height; i++)
  {
    for (int j = height; j >= i; j--)
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
  printf("\n");
  revrse_build(height);

  return 0;
}
