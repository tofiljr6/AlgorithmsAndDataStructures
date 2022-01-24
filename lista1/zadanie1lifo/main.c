#include <stdio.h>
#include <stdlib.h>

//LIFO
struct Node {
    int value;
    struct Node *next;
};

typedef struct Node *List;

/**
 * The method pushs value to the begginng of the list
 * @param ptr pointer to list
 * @param value value to put
 * @return returns new list with new value
 */
List push(List ptr, int value) {
    List new;
    new = malloc(sizeof(struct Node));
    new->value = value;
    new->next = ptr;
    return new;
}

/**
 * The method pritns value in the list
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
 * The method pops the value, prints it and return it
 * @param ptr pointer to the list
 * @return return poped value
 */
int pop(List ptr) {
    int v;

    if (ptr == NULL) {
        printf("Brak elementów\n");
    } else {
        v = ptr->value;
        printf("Sciągany element to: %d\n", v);
        (*ptr) = (*ptr->next);
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

//    pop(ptr);
//    print(ptr);

    return 0;
}
