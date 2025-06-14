#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
  int number;
  struct node *next;
}
next;

int main(int argc, char **argv)
{
  node *list = NULL;

  for (int i = 1; i < argc; i++)
  {
    int num = argv[i]; // initializing the value of pointer

    node *temp = malloc(sizeof(node)); // allocating memory for the temporary pointer that will point at nodes

    // securing program if some error occoured
    if (temp == NULL)
    {
      return 1;
    }

    // pointing at the space(number) allocated for the temp pointer an allocating number 
    temp->number = num;
    // initializing the pointer in the node to null, so that no garbage value will be asigned to it
    temp->next = NULL;

    temp->next = list; // making sure that the the temp is pointing at something so that we dont lose the prevous value
    // that is preventing memory leak
    list = temp; // finnay can we initialize the correct value 
  }
}
