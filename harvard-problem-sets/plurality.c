#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int prototype(int arr[], int size)
{
  int max = arr[0];

  for (int i = 0; i < size; i++)
  {
    if (arr[i] > max)
    {
      max = arr[i];
    }
  }
  return max;
}

int findMax(int arr[], int size)
{
  int max = arr[0];
  
  for (int i = 0; i < size; i++)
  {
    if (arr[i] > max)
    {
      max = arr[i];
    }
  }
  return max;
}


int findIndx(int arr[], int size, int target)
{
  for (int i = 0; i < size; i++)
  {
    if (arr[i] == target)
    {
      return i;
    }
  }
  return -1;
}

void rmElement(char *arr[], int *size, int index)
{
  if (index < 0 || index > *size)
  {
    printf("Invalid Index");
    return;
  }

  for (int i = index; i < *size - 1; i++)
  {
    arr[i] = arr[i+1];
  }
  (*size)--;
}

int main(int argc, char *argv[])
{
  if (argc < 2)
  {
    printf("NO arguments passed!");
    return 1;
  }
  
  // Managing argv is the most important part here Lol and forgot that
  // I was killing myself ovetr it,
  // i have never been so anxious, but here we go, the solution is clear now!

  printf("Number of voters: ");
  int num;
  scanf("%d", &num);
  int parallel[num];
  

  int size = argc;
  int index = 0;
  
  rmElement(argv, &size, index);

  for (int i = 0; i < size; i++)
  {
    printf("%s\n", argv[i]);
  }
  for (int i = 0; i < num; i++)
  {
    parallel[i] = 0;
  }

  for (int i = 0; i < num; i++)
  {
    printf("Vote: ");
    char vote[20];
    scanf("%s", vote);
    for (int j = 0; j < size; j++) 
    {
      if (strcmp(vote, argv[j]) == 0)
      {
        parallel[j] += 1;
        break;
      }
    }
  }


  for (int i = 0; i < num; i++)
  {
    printf("parallel_%d: %d\n", i, parallel[i]);
  }

  int max;
  max = findMax(parallel, num);
  printf("max: %d\n", max);


  int indx;
  indx = findIndx(parallel, num, max);
  printf("index: %d\n", indx);

  printf("%s\n", argv[indx]);
  
  return 0;
    
}
