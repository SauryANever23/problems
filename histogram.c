/*
*Write a program to print a histogram of the lengths of words in its input. It is
easy to draw the histogram with the bars horizontal;
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 200 

int main(void)
{
  char sentence[MAX];
  printf("Enter sentence: ");
  fgets(sentence, MAX, stdin); 
  int len, i;
  i = 0;
  while (sentence[i]!='\0')
  {
    len++;
    i++;
  }


}
