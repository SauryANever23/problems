#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
  int number;
  struct node *next;
}
node;

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

  // Now printing the values stored in the linked list

  // initializing a temprary pointer that will point that the first value of list
  node *ptr = list;

  // we will constatbly change the value of pointer untill the pointer reaches the value of NULL(the last 'next' block)
  while (ptr != NULL)
  {
    printf("%d\n", ptr->number); // printing the number assigned to the first value of list in the node

    // updating the ptr so that it points to another value in the linked list. 
    ptr = ptr->next; 
  }
  
  // Now, as our duty, I am freeing the allocated memory
  ptr = list; // assigning the the value of ptr as that of list

  while (ptr != NULL)
  {
    node *next = ptr; // This is a kller move right here. Adding anoter temporary variable for a temporary variable that will
    // point at the momory we want to free, but will not lose where we want to go next
    free(ptr);
    ptr = next;
  }
  return 0;
}
