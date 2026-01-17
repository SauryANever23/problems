/*
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.
*/

#include <stdio.h> 
#include <string.h> 
#include <ctype.h> 

#define MAX 100 

int main(void)
{
  char str1[MAX], str2[MAX];
  scanf("%s\n%s", str1, str2);
  
  int len = strlen(str1); 
  for (int i = 0; str1[i] != '\0'; i++) 
  {
    str1[i] = tolower((unsigned char)str1[i]);
    str2[i] = tolower((unsigned char)str2[i]);
  }

  int change = 0;
  for (int i = 0; i < len; i++)
  {
    int val = str1[i]-str2[i];
    if (val==0)
    {
      change = 0;   
    }
    else if (val>0)
    {
      change = 1;
      break;
    }
    else if (val < 0)
    {
      change = -1;
      break;
    }
  }
  printf("%d\n",change);
  return 0;
}

