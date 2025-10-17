/* 
*
* First Take in words 
* then make a histogram of word lenths (horizontally)
* Taking words: and use stars to make different sizes
* '*' for freaquency 
* '1', '2', etc for the class
*/


#include <stdio.h> 

#define MAX 20 

// using a key value pair JUST in case
typedef struct 
{
  int number;
  int freaquency;
}
key;

int main(void)
{
  int c;
  int current_word_len = 0;
  int word_len_arry[MAX + 1] = {0};

  while ((c=getchar()) != EOF)
  {
    if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
    {
      current_word_len++;
    }

    else if (c == ' ' || c == '\n' || c == '\t')
    {
      if (0 < current_word_len <= MAX)
      {
        word_len_arry[current_word_len]++;
      }
      current_word_len = 0;
    }

    if (current_word_len > 0 && current_word_len <= MAX)
    {
      word_len_arry[current_word_len]++;
    }    
  }

  for (int i = 0; i <= MAX; i++)
  {
    printf("Word len %d: %d\n", i, word_len_arry[i]);
    // if (word_len_arry[i] != 0)
    // {
      // // printf("Word Len %d: ", i);
      // for (int j = 0; j <= i; j++)
      // {
      //   printf("*");
      // }
      // printf("\n");
     // }
  }
}
