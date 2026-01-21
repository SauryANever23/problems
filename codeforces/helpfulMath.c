/*
*Xenia the beginner mathematician is a third year student at elementary school. She is now learning the addition operation.

The teacher has written down the sum of multiple numbers. Pupils should calculate the sum. To make the calculation easier, the sum only contains numbers 1, 2 and 3. Still, that isn't enough for Xenia. She is only beginning to count, so she can calculate a sum only if the summands follow in non-decreasing order. For example, she can't calculate sum 1+3+2+1 but she can calculate sums 1+1+2 and 3+3.

You've got the sum that was written on the board. Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.

Input
The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces. It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3. String s is at most 100 characters long.

Output
Print the new sum that Xenia can count.
*/
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

#define MAX 100

int main(void)
{
  char str[MAX]; 
  scanf("%s",str); 
  int len=0;
  int arr[MAX];

  for (int i = 0; str[i]!='\0'; i++)
  {
    if (str[i]!='+')
    {
      arr[i]=str[i]-'0';
      len++;
    }
  }
 
  // Bubble sort to sort the array
  for (int i = 0; i < count - 1; i++)
  {
    for (int j = 0; j < count - 1 - i; j++)
    {
      if (arr[j] > arr[j + 1])
      {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }


  for (int i = 0; i < len; i++)
  {
    if (i < len-1)
    {
      printf("%d+", arr[i]);
    }
    else
    {
      printf("%d\n",arr[i]);  
    }
  }
  printf("\n");

  return 0;
}
