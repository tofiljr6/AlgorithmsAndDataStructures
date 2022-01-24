#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

// lista dwukierunkowa cykliczna
struct Node {
    int value;
    struct Node *next;
    struct Node *previous;
};

typedef struct Node *List;

struct ListInfo {
    struct Node *head;
    struct Node *tail;
};

typedef struct ListInfo *Info;


/**
 * The method adds the value to the list
 * @param info pointer to the info of list
 * @param value value to put in
 * @return return new info of list with put value
 */
Info add3(Info info, int value) {
    List new;
    new = malloc(sizeof(struct Node));
    new->value = value;

    Info infoResult;
    infoResult = malloc(sizeof(struct ListInfo));
    struct Node *h;
    struct Node *t;

    h = info->head;
    t = info->tail;

    if (h == NULL) {
        new->next = new;
        new->previous = new;
        h = new;
        t = new;
    } else {
        new->next = h;
        new->previous = t;
        t->next = new;
        h->previous = new;
        t = new;
    }

    infoResult->head = h;
    infoResult->tail = t;
    return infoResult;
}

/**
 * The method prints the list in right direction
 * @param info pointer to the info of list
 */
void pt(Info info) {
    printf("List printing: \n");
    List tmp = info->head;

    if (tmp != NULL) {
        do {
            printf("%d ", tmp->value);
            tmp = tmp->next;
        } while (tmp != info->head);
    } else {
        printf("Brak elementów\n");
    }

    printf("\n");
}

/**
 * The method prints the list in left direction (reverse)
 * @param info pointer to the info of list
 */
void ptReverse(Info info) {
    printf("List reverse printing: \n");
    List tmp = info->tail;

    if (tmp != NULL) {
        do {
            printf("%d ", tmp->value);
            tmp = tmp->previous;
        } while (tmp != info->tail);
    } else {
        printf("Brak elementów\n");
    }

    printf("\n");
}

/**
 * The method return the lenght of list
 * @param info pointer to the info of list
 * @return lenght of list
 */
int len(Info info) {
    List tmp = info->head;
    int l = 0;
    do {
        tmp = tmp->next;
        l++;
    } while (tmp != info->head);
    return l;
}

/**
 * The method tests periodic of the list
 * @param info pointer to the info of list
 */
void periodicTest(Info info) {
    printf("Periodic test: \n");
    List tmp = info->head;
    for (int i = 0; i < 2 * len(info); i++) {
        printf("%d ", tmp->value);
        tmp = tmp->next;
    }
}

/**
 * The method merges two lists
 * @param info1 pointer to the info of list 1
 * @param info2 pointer to the info of list 2
 * @return new merged list
 */
Info merge(Info info1, Info info2) {
    Info mergeInfo;

    mergeInfo = info1;

    mergeInfo->tail->next = info2->head;
    info2->head->previous = mergeInfo->tail;

    mergeInfo->head->previous = info2->tail;
    info2->tail->next = mergeInfo->head;

    return mergeInfo;
}

/**
 * The method counts how many step is to the first value
 * @param info pointer to the info of list
 * @param value is looked for
 * @return steps
 */
int steps(Info info, int value) {
    List tmp = info->head;
    int l = 0;
    int steps = 0;
    do {
        if (value == steps) {
            return steps;
        }
        steps++;
        l++;
        tmp = tmp->next;
    } while (tmp != info->head);
    return -1;
}

/**
 * The method counts how many step is to the i-index
 * @param info pointer to the info of list
 * @param value index of lists
 * @return steps
 */
int find(Info info, int value) {
    List tmp = info->head;
    int l = 0;
    int steps = 1;
    do {
        if (value == tmp->value) {
            return steps;
        }
        steps++;
        l++;
        tmp = tmp->next;
    } while (tmp != info->head);
    return steps;
}

int main() {
    srand(time(NULL));

    Info info1, info2, mergeInfo, testPeriodic, i1, i2, i12;
    info1 = malloc(sizeof(struct Node));
    info2 = malloc(sizeof(struct Node));
    i1 = malloc(sizeof(struct Node));
    i2 = malloc(sizeof(struct Node));
    testPeriodic = malloc(sizeof(struct Node));

    testPeriodic = add3(testPeriodic, 6);
    testPeriodic = add3(testPeriodic, 11);
    testPeriodic = add3(testPeriodic, 16);

    pt(testPeriodic);
    ptReverse(testPeriodic);
    periodicTest(testPeriodic);

    printf("\n\n");

    i1 = add3(i1, 58);
    i1 = add3(i1, 108);
    i1 = add3(i1, 158);

    i2 = add3(i2, 34);
    i2 = add3(i2, 64);
    i2 = add3(i2, 94);

    pt(i1);
    pt(i2);
    printf("Długośc tablicy drugiej to: %d\n", len(i2));
    i12 = merge(i1, i2);
    pt(i12);
    ptReverse(i12);
    i2 = add3(i2, 100);
    pt(i2);
    ptReverse(i2);

    for (int i = 0; i < 1000; i++) {
        info1 = add3(info1, i);
        info2 = add3(info2, rand() % 20 + 20);
    }

    for (int j = 0; j < 5; j++) {
        printf("Attempt number %d\n", j);
        for (int i = 0; i < 5; i++) {
            printf("Access to element number: %d in %d steps\n", (i + 1) * 100, steps(info1, (i + 1) * 100));
        }
        int r = rand() % 1000;
        printf("Access to element number: %d in %d steps\n", r, steps(info1, r));
    }

//    mergeInfo = merge(info1, info2);
//    pt(mergeInfo);

    int suma = 0;

    for (int i=1; i<1000; i++) {
        int x = find(info1, rand() % 1000);
        suma += x;

    }

    printf("Srednia ilośc kroków do losowo wybranego elementu: %f\n", (float) suma/1000);

    return 0;
}
