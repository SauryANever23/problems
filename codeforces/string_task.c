/*
 *Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

deletes all the vowels,
inserts a character "." before each consonant,
replaces all uppercase consonants with corresponding lowercase ones.
Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

Help Petya cope with this easy task.

Input
The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

Output
Print the resulting string. It is guaranteed that this string is not empty.
 */

#include <stdio.h> 
#include <string.h>
#include <ctype.h>

#define MAX 100

int main(void)
{
  char str[MAX];
  scanf("%s", str); 
  char spare[MAX];
  char final[MAX];
  strcpy(spare, str);
  for (int i = 0; i <= strlen(str); i++)
  {
    if (tolower(str[i]) != 'a' || tolower(str[i]) != 'e' || tolower(str[i]) != 'i' || tolower(str[i]) != 'o' || tolower(str[i]) != 'u' || tolower(str[i]) != 'y')
    {
      final[i] = "."+str[i]
    }
  }
  printf("%s\n", final);

  return 0;
}
