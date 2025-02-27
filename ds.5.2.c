#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 100

struct stack {
    int stArr[MAXSIZE]; 
    int top;
};

typedef struct stack STACK;

void create(STACK* s) {
    s->top = -1;  
    printf("Stack created successfully.\n");
}

int isFull(STACK* s) {
    return s->top == MAXSIZE - 1;
}

int isEmpty(STACK* s) {
    return s->top == -1;
}

void push(STACK* s, int data) {
    if (isFull(s)) {
        printf("Stack Overflow! Cannot push %d\n", data);
        return;
    }
    s->stArr[++(s->top)] = data;  
    printf("Pushed %d onto the stack.\n", data);
}

int pop(STACK* s) {
    if (isEmpty(s)) {
        printf("Stack Underflow! Stack is empty.\n");
        return -1;
    }
    int poppedValue = s->stArr[(s->top)--];
    printf("Popped %d from the stack.\n", poppedValue);
    return poppedValue;
}

int peek(STACK* s) {
    if (isEmpty(s)) {
        printf("Stack is empty. Cannot peek.\n");
        return -1;  
    }
    return s->stArr[s->top];  
}

int main() {
    STACK s;  
    create(&s); 

    int choice, value;

    while (1) {
        printf("\nStack Operations:\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Peek\n");
        printf("4. Check if Stack is Full\n");
        printf("5. Check if Stack is Empty\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the value to push: ");
                scanf("%d", &value);
                push(&s, value);
                break;
            case 2:
                pop(&s);
                break;
            case 3:
                value = peek(&s);
                if (value != -1) {
                    printf("Top element is: %d\n", value);
                }
                break;
            case 4:
                if (isFull(&s)) {
                    printf("Stack is Full.\n");
                } else {
                    printf("Stack is not Full.\n");
                }
                break;
            case 5:
                if (isEmpty(&s)) {
                    printf("Stack is Empty.\n");
                } else {
                    printf("Stack is not Empty.\n");
                }
                break;
            case 6:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
