from math import floor
import sys
import fileinput


def insertionSort(A):
    """The method sorts A - array in insertion sort way"""
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def mergeSort(A):
    """The method sorts A - array in merge sort way"""
    if len(A) > 1:
        return merge(mergeSort(A[:floor(len(A)/2)]), mergeSort(A[floor((len(A)/2)):]))
    else:
        return A


def merge(C, D):
    """The method merge two sorted arrays keeping them still sorted"""
    if len(C) == 0:
        return D
    if len(D) == 0:
        return C
    if C[0] <= D[0]:
        return C[0:1] + merge(C[1:], D)
    else:
        return D[0:1] + merge(C, D[1:])


def quickSort(A, p, r):
    """The method sorts A - array in quick sort way QS(A,0,len(A)-1)"""
    if p < r:
        q = partitionHoare(A, p, r)
        quickSort(A, p, q)
        quickSort(A, q+1, r)


def partitionHoare(A, low, high):
    pivot = A[floor((low+high)/2)]
    i = low - 1
    j = high + 1

    while True:
        while True:
            i += 1
            if A[i] >= pivot:
                break

        while True:
            j -= 1
            if A[j] <= pivot:
                break

        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]


x = [1,5,10,13,6,3,2,8,11,4]


def finalCheck(A):
    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            return False
    return True



# print(quickSort(x, 0, len(x) - 1))
# print(partitionHoare(x, 0, len(x) -1))

# print(quickSort(x, 0, len(x) - 1))
# print(x)

# cmp = -1
#
def do_work():
    """ Function to handle command line usage"""

    elements = int(input("Podaj ilość elementów w tablicy: "))
    print("Tablica rozmiaru: ", elements)
    array = list()
    for element in range(elements):
        array.append(int(input()))
    print("Wpisana tablica:", array)

    decision = list()

    args = sys.argv
    args = args[1:] # First element of args is the file name
    if len(args) == 0:
        print('You have not passed any commands in!')
    else:
        for i in range(len(args)):
            if args[i] == '--help':
                print('Basic command line program')
                print('Options:')
                print('    --help -> show this basic help menu.')
                print('    --monty -> show a Monty Python quote.')
                print('    --veg -> show a random vegetable')
            elif args[i] == '--type':
                if args[i+1] == 'quick':
                    decision.append(1)
                    print('quicksort')
                elif args[i+1] == 'merge':
                    decision.append(2)
                    print('mergesort')
                    y = mergeSort(array)
                    print('Result', y, finalCheck(y))
                elif args[i+1] == 'insert':
                    print('insert')
                else:
                    print("Unrecogniezed algoritm to sorting")
            elif args[i] == '--comp':
                if args[i+1] == '>=':
                    decision.append(4)
                    cmp = 0
                    print('desc')
                elif args[i+1] == '<=':
                    decision.append(5)
                    print('ascending')
                    cmp = 1



if __name__ == '__main__':
    do_work()
