from math import floor
import sys
import time
import random


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


def insertionSort(A, dec):
    """ The method sorts A - array in insertion sort way.
        A method returns array in 'dec' order.
    """
    comparison = 0
    substitution = 0
    for j in range(1, len(A)):
        key = A[j] # I count this substitution later - end of the method
        i = j - 1

        # compare in while
        comparison += 1
        while i > -1 and compare(key, A[i], dec):
            # substitute
            A[i + 1] = A[i]
            substitution += 1

            i -= 1
        # substitute key value
        A[i + 1] = key
        # sys.stderr.write("%s\n" % A)
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

    # mergecomp += 1
    if len(A) > 1:
        # sys.stderr.write("DIVIDE %s\n" % A)
        L = mergeSort(A[:floor(len(A)/2)], dec)
        R = mergeSort(A[floor(len(A)/2):], dec)
        # sys.stderr.write("CONQUER %s + %s = " % (L, R))
        MLR = merge(L, R, dec)
        # sys.stderr.write("%s\n" % MLR)
        return MLR
    else:
        return A


def merge(C, D, dec):
    """ The method merge two sorted arrays keeping them still sorted.
        A method helps in main algoritm mergeSort.
    """
    n1 = len(C)
    n2 = len(D)
    E = [None] * (n1 + n2)
    i, j, k = 0, 0, 0

    global mergecomp, mergesub

    while i < n1 and j < n2:
        mergecomp += 1
        mergesub += 1
        if compare(C[i], D[j], dec):
            E[k] = C[i]
            i += 1
        else:
            E[k] = D[j]
            j += 1
        k += 1

    while i < n1:
        mergesub += 1
        E[k] = C[i]
        k += 1
        i += 1

    while j < n2:
        mergesub += 1
        E[k] = D[j]
        k += 1
        j += 1

    return E



quicksub = 0 # substitution in quicksort algorithm
quickcomp = 0 # comparison in quicksort algorithm


def quickSort(A, p, r, dec):
    """ The method sorts A - array in quick sort way QS(A,0,len(A)-1).
    """
    # i dont interprated lenght of array as comparison
    global quickcomp

    # quickcomp += 1
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
            # pretty print - commented because it dirt result in second exercises
            # sys.stderr.write("I: if %s %s %s \n" % (pivot, dec, A[i]))
            if compare(pivot, A[i], dec):
                break

        while True:
            j -= 1

            quickcomp += 1
            # pretty print - commented because it dirt result in second exercises
            # sys.stderr.write("J: if %s %s %s \n" % (A[j], dec, pivot))
            if compare(A[j], pivot, dec):
                break

        # quickcomp += 1
        if i >= j:
            return j

        quicksub += 1
        # pretty print - commented because it dirt result in second exercises
        # sys.stderr.write("A: %s swap %s <-> %s \n" % (A, A[i], A[j]))
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
    """ Function load elements from command line
    """
    elements = int(input())
    array = list()
    for element in range(elements):
        array.append(int(input()))
    return array


def writeStdErrSubsAndComp(sub, comp, sorted, deltat):
    """ Function writes on standard error output numbers of substitution and comparison
    """
    print("Number of substitution: %s" % sub)
    print("Number of comparison: %s" % comp)

    sys.stderr.write("Number of substitution: %s \n" % sub)
    sys.stderr.write("Number of comparison: %s \n" % comp)
    sys.stderr.write("It is sorted? %r \n" % sorted)
    sys.stderr.write("Time: %s s \n" % deltat)


def generateRandomArrays(k):
    n = [i * 100 for i in range(1, 101)]
    listarrays = list()
    for kprim in range(k):
        for en in n:
            listarrays.append(list([random.randint(1,1000) for j in range(en)]))
    return listarrays

def doWork():
    """ Function to handle command line usage.
    """
    # input array
    array = list()

    sortAlg = 0
    sortOrder = 0
    kRepeats = 0

    # I reset values in --stat
    global quicksub, quickcomp
    global mergesub, mergecomp

    # command handler
    args = sys.argv
    args = args[1:] # first element of args is the file name
    if (len(args) == 0):
        # may deflaut sorting
        print('You have not passed any commands in!')
    else:
        if "--stat" not in args:
            array = loadArray()

        for i in range(len(args)):
            if args[i] == "--type":
                if args[i+1] in ["quick", "merge", "insert"]:
                    sortAlg = args[i+1]
            elif args[i] == "--comp":
                if args[i+1] in [">=", "<="]:
                    sortOrder = args[i+1]
            elif args[i] == "--stat":
                file = open(args[i+1], "w")

                # TODO: generate random arrays
                grd = generateRandomArrays(int(args[i+2]))
                # print(grd)

                kRepeats = int(args[i+2])
                # file.write(args[i+2])
                # print("--stat", args[i+2])

    # execution if --stat not in command line
    if "--stat" not in args:
        if sortAlg == "quick":
            # time measure
            start = time.time()
            quickSort(array, 0, len(array) - 1, sortOrder)
            stop = time.time()

            # std error output + pirnts array
            sys.stderr.write("A: %s \n" % array)
            writeStdErrSubsAndComp(quicksub,
                                   quickcomp,
                                   finalCheck(array, sortOrder),
                                   round(stop - start, 20))
        elif sortAlg == "merge":
            # time measure
            start = time.time()
            array = mergeSort(array, sortOrder)
            stop = time.time()

            # std error output
            writeStdErrSubsAndComp(mergesub,
                                   mergecomp,
                                   finalCheck(array, sortOrder),
                                   round(stop - start, 20))
        elif sortAlg == "insert":
            # example sample - only for test
            # arr = [random.randint(1, 20) for i in range(50000)]

            # time measure
            start = time.time()
            tmp = insertionSort(array, sortOrder)
            stop = time.time()

            array = tmp[0]
            insertcomp = tmp[1]
            insertsub = tmp[2]

            # std error output
            writeStdErrSubsAndComp(insertsub,
                                   insertcomp,
                                   finalCheck(array, sortOrder),
                                   round(stop - start, 20))

        print("Sorted array: ", sortAlg,  sortOrder, "->", array )
    else:
        for g in grd:
            ## HOW TO REFACTOR THIS?
            # quicksort
            x = g.copy()
            start = time.time()
            quickSort(x, 0, len(x) - 1, sortOrder)
            stop = time.time()
            dt = round(stop - start, 10)
            print("QUICK:", g, x, "substitution:", quicksub, "comparistion", quickcomp)
            r = "QUICK: " + str(len(g)) + " " + str(quicksub) + " " + str(quickcomp) + " " + str(dt) + "\n"
            file.write(r)
            quicksub, quickcomp = 0, 0

            # mergeSort
            x = g.copy()
            start = time.time()
            xResult = mergeSort(x, sortOrder)
            stop = time.time()
            dt = round(stop - start, 10)
            print("MERGE:", g, xResult, "substitution:", mergesub, "comparistion", mergecomp)
            r = "MERGE: " + str(len(g)) + " " + str(mergesub) + " " + str(mergecomp) + " " + str(dt) + "\n"
            file.write(r)
            mergesub, mergecomp = 0, 0

            # insertionSort
            x = g.copy()
            start = time.time()
            xResult = insertionSort(x, sortOrder)
            stop = time.time()
            dt = round(stop - start, 10)
            print("INSERT:", g, xResult[0],  "substitution:", xResult[2], "comparistion", xResult[1])
            r = "INSERT: " + str(len(g)) + " " + str(xResult[2]) + " " + str(xResult[1]) + " " + str(dt) + "\n"
            file.write(r)

            file.write("\n")


        file.close()


if __name__ == '__main__':
    doWork()
