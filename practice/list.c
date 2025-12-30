#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    string phrase;
    struct node *next;
} node;

// Function to display the linked list
void display_list(node *list) {
    node *current = list;
    node *previous = NULL; // Pointer to track the previous node

    while (current != NULL) {
        printf("Current Node Address: %p, Phrase: %s\n", (void *)current, current->phrase);
        if (previous != NULL) {
            printf("Previous Node Address: %p\n", (void *)previous);
        } else {
            printf("Previous Node Address: NULL\n");
        }
        previous = current; // Update previous to the current node
        current = current->next; // Move to the next node
    }
}

int main(void) {
    node *list = NULL;

    // Adding first node
    node *temp = malloc(sizeof(node));
    if (temp == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    string value1 = get_string("Enter a phrase to be entered: ");
    temp->phrase = value1;
    temp->next = list;
    list = temp;

    // Adding second node
    temp = malloc(sizeof(node));
    if (temp == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    string value2 = get_string("Enter a phrase to be entered: ");
    temp->phrase = value2;
    temp->next = list;
    list = temp;

    // Display the linked list
    printf("Linked list contents:\n");
    display_list(list);

    // Free the allocated memory
    while (list != NULL) {
        node *next = list->next;
        free(list);
        list = next;
    }

    return 0;
}
