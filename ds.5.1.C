#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        return NULL;
    }
    newNode->data = data;
    newNode->next = newNode; 
    return newNode;
}

void insertAtBeginning(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        struct Node* temp = *head;
        while (temp->next != *head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = *head;
        *head = newNode;
    }
}

void insertAtLast(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        struct Node* temp = *head;
        while (temp->next != *head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = *head;
    }
}

void insertAtPosition(struct Node** head, int data, int position) {
    if (position <= 0) {
        printf("Invalid position\n");
        return;
    }
    if (position == 1) {
        insertAtBeginning(head, data);
        return;
    }
    struct Node* newNode = createNode(data);
    struct Node* temp = *head;
    int count = 1;
    while (temp != NULL && count < position - 1) {
        temp = temp->next;
        count++;
        if (temp == *head) {
            break;
        }
    }
    if (temp == NULL || temp->next == *head) {
        printf("Position out of bounds\n");
        return;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}

void deleteFromBeginning(struct Node** head) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct Node* temp = *head;
    if (temp->next == *head) {
        *head = NULL;
        free(temp);
    } else {
        struct Node* last = *head;
        while (last->next != *head) {
            last = last->next;
        }
        *head = temp->next;
        last->next = *head;
        free(temp);
    }
}

void deleteFromLast(struct Node** head) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct Node* temp = *head;
    if (temp->next == *head) {
        *head = NULL;
        free(temp);
    } else {
        while (temp->next->next != *head) {
            temp = temp->next;
        }
        struct Node* last = temp->next;
        temp->next = *head;
        free(last);
    }
}

void deleteFromPosition(struct Node** head, int position) {
    if (position <= 0 || *head == NULL) {
        printf("Invalid position or list is empty\n");
        return;
    }
    if (position == 1) {
        deleteFromBeginning(head);
        return;
    }
    struct Node* temp = *head;
    struct Node* prev = NULL;
    int count = 1;
    while (temp != NULL && count < position) {
        prev = temp;
        temp = temp->next;
        count++;
        if (temp == *head) {
            break;
        }
    }
    if (temp == NULL || prev == NULL || temp == *head) {
        printf("Position out of bounds\n");
        return;
    }
    prev->next = temp->next;
    free(temp);
}

void display(struct Node* head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct Node* temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(head)\n");
}

int main() {
    struct Node* head = NULL;
    int choice, data, position;

    while (1) {
        printf("\nCircular Linked List Operations:\n");
        printf("1. Insert at Beginning\n");
        printf("2. Insert at Last\n");
        printf("3. Insert at Specific Position\n");
        printf("4. Delete from Beginning\n");
        printf("5. Delete from Last\n");
        printf("6. Delete from Specific Position\n");
        printf("7. Display List\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data to insert at beginning: ");
                scanf("%d", &data);
                insertAtBeginning(&head, data);
                break;
            case 2:
                printf("Enter data to insert at last: ");
                scanf("%d", &data);
                insertAtLast(&head, data);
                break;
            case 3:
                printf("Enter data to insert and position: ");
                scanf("%d %d", &data, &position);
                insertAtPosition(&head, data, position);
                break;
            case 4:
                deleteFromBeginning(&head);
                break;
            case 5:
                deleteFromLast(&head);
                break;
            case 6:
                printf("Enter position to delete: ");
                scanf("%d", &position);
                deleteFromPosition(&head, position);
                break;
            case 7:
                display(head);
                break;
            case 0:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
