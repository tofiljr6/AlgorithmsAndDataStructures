#include <stdio.h>
#include <stdlib.h>

// FIFO
struct Node {
    int value;
    struct Node *next;
};

typedef struct Node *List;

/**
 * The method pushs the value to the list
 * @param ptr pointer to the list
 * @param value value to put in
 * @return returns the new list with new value
 */
List push(List ptr, int value) {
    List new;
    new = malloc(sizeof(struct Node));
    new->value = value;
    new->next = ptr;
    return new;
}

/**
 * The method prints the list
 * @param ptr pointer to the list
 */
void print(List ptr) {
    printf("List: ");
    while (ptr != NULL) {
        printf("%d ", ptr->value);
        ptr = ptr->next;
    }
    printf("\n");
}

/**
 * The method pops the value form list, printns it and returns it
 * @param ptr pointer to the list
 * @return return the poped value
 */
int pop(List ptr) {
    List tmp;
    tmp = malloc(sizeof(struct Node));
    int v;

    if (ptr == NULL) {
        printf("Brak elementów\n");
        return -1;
    }

    while(ptr != NULL) {
        if (ptr->next == NULL) {
            printf("Ściagany element: %d\n", ptr->value);
            v = ptr->value;
            ptr = tmp;
            ptr->next = NULL;
        }
        tmp = ptr;
        ptr = ptr->next;
    }
    return v;
}


int main() {
    List ptr = NULL;

    pop(ptr);

    for (int i = 0; i < 100; i++) {
        ptr = push(ptr, i);
    }

    print(ptr);

    for (int i = 0; i < 100; i++) {
        pop(ptr);
    }

//    print(ptr);
//    pop(ptr);
//    print(ptr);
//    ptr = push(ptr, 40);
//    print(ptr);
//    pop(ptr);
//    print(ptr);



    return 0;
}
