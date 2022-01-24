#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// lista jednokierunkowa
struct Node {
    int value;
    struct Node *next;
};

typedef struct Node *List;

/** The method prints the all values in list
 *
 * @param ptrpointer to the list
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
 * The method adds value to the beginning od the list
 *
 * @param ptr pointer to the list
 * @param val new value added to the beginning of the list
 * @return return new list
 */
List addBeginning(List ptr, int val) {
    List new;
    new = malloc(sizeof(struct Node));
    new->value = val;
    new->next = ptr;
    return new;
}

/**
 * The method adds value to the end of the list
 *
 * @param ptr pointer to the list
 * @param value new value added to the end of the list
 */
void addEndinng(List *ptr, int value) {
    List new, tmp;
    new = malloc(sizeof(struct Node));
    new->value = value;
    new->next = NULL;

    if (*ptr == NULL) {
        *ptr = new;
    } else {
        tmp = *ptr;
        while (tmp->next != NULL) {
            tmp = tmp->next;
        }
        tmp->next = new;
    }
}

/**
 * The method deletes all list
 * @param ptr pointer to the list
 */
void delete(List *ptr) {
    List tmp;
    while(*ptr != NULL) {
        tmp = (*ptr)->next;
        free(*ptr);
        *ptr = tmp;
    }
}

/** The method searchs the value and returns number of steps to get the value
 *
 * @param ptr pointer to the list
 * @param value value we want to get to to
 * @return number of steps to get the value
 */
int search(List ptr, int value) {
    int steps = 0;
    while (ptr != NULL) {
        if (ptr->value == value) {
            return steps;
        }
        steps++;
        ptr = ptr->next;
    }
    return steps;
}

/**
 * The method merge two list
 * @param ptr1 pointer to the list number 1
 * @param ptr2 pointer to the list number 2
 * @return return merged list of two lists
 */
List merge(List *ptr1, List *ptr2) {
    List tmp = NULL;
    if (*ptr1 == NULL) {
        *ptr1 = *ptr2;
    } else {
        tmp = *ptr1;
        while (tmp->next != NULL) {
            tmp = tmp->next;
        }
        tmp->next = *ptr2;
    }
    return *ptr1;
}

/**
 * The method returns the numbers of steps to the elements of the number x
 * @param ptr pointer to the list
 * @param index index we what to check
 * @return number of steps
 */
int getStepsToGetIndex(List *ptr, int index) {
    int steps = 0;
    int i = 0;
    List tmp = NULL;
    if (*ptr == NULL) {
        return -1;
    } else {
        tmp = *ptr;
        while (tmp->next != NULL) {
            tmp = tmp->next;
            if (index == i) {
                return steps;
            }
            steps++;
            i++;
        }
    }
    return 0;
}

int main() {
    srand(time(NULL));

    // create new lists
    List ptr, ptr2, mergeResult, timePtr;
    ptr = NULL, ptr2 = NULL, mergeResult = NULL, timePtr = NULL;

    // fill list with random number
    for (int i = 0; i < 1000; i++) {
        ptr = addBeginning(ptr, rand() % 20);
        ptr2 = addBeginning(ptr2, rand() % 20 + 20);
        timePtr = addBeginning(timePtr, i);
    }

    // testing the number of steps to elements x
    for (int j = 0; j < 5; j++) {
        printf("Attempt number %d\n", j);
        for (int i = 0; i < 5; i++) {
            printf("Access to element number: %d in %d steps\n", (i + 1) * 100, getStepsToGetIndex(&ptr, (i + 1) * 100));
        }
        int r = rand() % 1000;
        printf("Access to element number: %d in %d steps\n", r, getStepsToGetIndex(&ptr, r));
    }

    // testing merging
    mergeResult = merge(&ptr, &ptr2);
    print(mergeResult);


    int suma = 0;
    for (int j = 1; j < 1000; j++) {
        int r = rand() % 1000;
        int x = getStepsToGetIndex(&timePtr, r);
        suma += x;
//        printf("%f\n", (float) suma/j);
    }

    printf("Srednia ilość kroków do wybranego losowe elementu wynosi: %f", (float) suma/999);

    return 0;
}