#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
    int data;
    struct Node* next;
};

struct Stack {
    struct Node* top;
};

struct Stack* create() {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->top = NULL;  
    return stack;
}

void push(struct Stack* stack, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = stack->top;
    stack->top = newNode;        
    printf("%d pushed to stack\n", value);
}

int pop(struct Stack* stack) {
    if (stack->top == NULL) {
        printf("Stack is empty, cannot pop\n");
        return -1;  
    }
    struct Node* temp = stack->top;
    int poppedValue = temp->data;
    stack->top = stack->top->next;  
    free(temp);  
    printf("%d popped from stack\n", poppedValue);
    return poppedValue;
}

int peek(struct Stack* stack) {
    if (stack->top == NULL) {
        printf("Stack is empty, no top element\n");
        return -1;  
    }
    return stack->top->data;  
}


bool isEmpty(struct Stack* stack) {
    return stack->top == NULL;  
}


bool isFull(struct Stack* stack) {
    return false;  
}

int main() {
    struct Stack* stack = create();  
    push(stack, 10);
    push(stack, 20);
    push(stack, 30);
    
    printf("Top element is %d\n", peek(stack)); 

    pop(stack);  
    printf("Top element is now %d\n", peek(stack));  
    
    pop(stack);
    pop(stack);

    if (isEmpty(stack)) {
        printf("The stack is empty.\n");
    } else {
        printf("The stack is not empty.\n");
    }

    return 0;
}
