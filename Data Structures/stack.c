/********************************************************************/
// The stack is a linear data structure that works of the LIFO principle
//
// The program below show an implmentation of a stack
// The program implements a Push, pop, isfull and isempty functions
// 
//
//
/********************************************************************/

#include <stdio.h>
#include <stdlib.h>

// The maximun number of elements in the stack
#define MAX 5

int count = 0;

// Creating a stack
typedef struct stack{
  int items[MAX];
  int top;
}stk;


void createEmptyStack(stk *s) {
  s->top = -1;
}

// Check if the stack is full
int isfull(stk *s) {
  if (s->top == MAX - 1)
    return 1;
  else
    return 0;
}

// Check if the stack is full
int isempty(stk *s) {
  if (s->top == - 1)
    return 1;
  else
    return 0;
}

// Add elements into stack
void push(stk *s, int newitem) {
  if (isfull(s)) {
    printf("STACK FULL");
  } else {
    s->top++;
    s->items[s->top] = newitem;
  }
  count++;
}

// Remove element from stack
void pop(stk *s) {
  if (isempty(s)) {
    printf("\n STACK EMPTY \n");
  } else {
    printf("Item popped = %d", s->items[s->top]);
    s->top--;
  }
  count--;
  printf("\n");
}

// Print elements of stack
void printStack(stk *s) {
  printf("Stack: ");
  for (int i = 0; i < count; i++) {
    printf("%d ", s->items[i]);
  }
  printf("\n");
}

// Driver code
int main() {
  int ch;
  stk *s = (stk *)malloc(sizeof(stk));

  createEmptyStack(s);

  push(s, 1);
  push(s, 2);
  push(s, 3);
  push(s, 4);

  printStack(s);

  pop(s);

  printf("\nAfter popping out\n");
  printStack(s);
}