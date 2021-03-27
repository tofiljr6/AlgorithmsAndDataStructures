from math import floor
import sys
from functools import wraps
from time import process_time
import timeit

# is this the best option to measure time on execution?
def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(process_time() * 1000000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(process_time() * 1000000)) - start
            print(
                f"Total execution time {func.__name__}: {end_ if end_ > 0 else 0} ms"
            )

    return _time_it


def compare(a, b, decison):
    """ The method compares two numbers and returns True or False accordign this rules:
        decision <= return True if a <= b
                    return False if a > b
        decision >= return True if a >= b
                    return False if a < b
    """
    if decison == "<=":
        return a <= b
    elif decison == ">=":
        return a >= b

# @measure
def insertionSort(A, dec):
    """ The method sorts A - array in insertion sort way.
        A method returns array in 'dec' order.
    """
    comparison = 0
    substitution = 0
    for j in range(1, len(A)):
        key = A[j] # I count this substitution later - end of the method
        i = j - 1
        while i > -1 and compare(key, A[i], dec):
            # compare in while
            comparison += 1

            # substitute
            A[i + 1] = A[i]
            substitution += 1

            i -= 1
        # substitute key value
        A[i + 1] = key
        substitution += 1
    return A, comparison, substitution

mergesub = 0 # substitution in merge algorithm
mergecomp = 0 # comparison in merge algorithm

def mergeSort(A, dec):
    """ The method sorts A - array in merge sort way.
        A method returns array in 'dec' order.
    """
    global mergecomp
    global mergesub # merge substitution equals 0 becasue i dont use it there

    mergecomp += 1
    if len(A) > 1:
        return merge(mergeSort(A[:floor(len(A)/2)], dec),
                     mergeSort(A[floor(len(A)/2):], dec), dec)
    else:
        return A


def merge(C, D, dec):
    """ The method merge two sorted arrays keeping them still sorted.
        A method helps in main algoritm mergeSort.
    """
    # i interprated lenght of array as comparison
    global mergecomp

    mergecomp += 1
    if len(C) == 0:
        return D

    mergecomp += 1
    if len(D) == 0:
        return C

    mergecomp += 1
    if compare(C[0], D[0], dec):
        return C[0:1] + merge(C[1:], D, dec)
    else:
        return D[0:1] + merge(C, D[1:], dec)


quicksub = 0 # substitution in quicksort algorithm
quickcomp = 0 # comparison in quicksort algorithm


def quickSort(A, p, r, dec):
    """ The method sorts A - array in quick sort way QS(A,0,len(A)-1).
    """
    global quickcomp
    quickcomp += 1
    if p < r:
        q = partitionHoare(A, p, r, dec)
        quickSort(A, p, q, dec)
        quickSort(A, q+1, r, dec)


def partitionHoare(A, low, high, dec):
    """ The method make partition in Hoare way.
    """
    pivot = A[floor((low+high)/2)]
    i = low - 1
    j = high + 1

    global quicksub, quickcomp

    while True:
        while True:
            i += 1

            quickcomp += 1
            if compare(pivot, A[i], dec):
                break

        while True:
            j -= 1

            quickcomp += 1
            if compare(A[j], pivot, dec):
                break

        quickcomp += 1
        if i >= j:
            return j

        quicksub += 1
        A[i], A[j] = A[j], A[i]


def finalCheck(A, dec):
    """ The method checks the result and confirms if array is sorted
    """
    for i in range(len(A) - 1):
        if not compare(A[i], A[i+1], dec):
            return False
    return True

ascending = "<="
descending = ">="


def loadArray():
    """ Function
    """
    elements = int(input("Podaj ilość elementów tablicy: "))
    array = list()
    for element in range(elements):
        array.append(int(input()))
    return array

def doWork():
    """ Function to handle command line usage.
    """
    # input array
    array = loadArray()

    sortAlg = 0
    sortOrder = 0

    # command handler
    args = sys.argv
    args = args[1:] # first element of args is the file name
    if (len(args) == 0):
        # may deflaut sorting
        print('You have not passed any commands in!')
    else:
        for i in range(len(args)):
            if args[i] == "--type":
                if args[i+1] in ["quick", "merge", "insert"]:
                    sortAlg = args[i+1]
            elif args[i] == "--comp":
                if args[i+1] in [">=", "<="]:
                    sortOrder = args[i+1]

    # execution
    if sortAlg == "quick":
        quickSort(array, 0, len(array) - 1, sortOrder)
    elif sortAlg == "merge":
        array = mergeSort(array, sortOrder)
    elif sortAlg == "insert":
        array = insertionSort(array, sortOrder)[0] 

    print("Sorted array: ", sortAlg, "->", array )

    print("I sort use: ", sortAlg, " in order", sortOrder)












if __name__ == '__main__':
    doWork()
