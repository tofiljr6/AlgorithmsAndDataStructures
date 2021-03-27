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
    print(A)
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

t = [2,5,7,0,1,2,7,3,9,5]
x = [2,5,7,0,1,2,7,3,9,5]
y = [2,5,7,0,1,2,7,3,9,5]
z = [2,5,7,0,1,2,7,3,9,5]
# w = [8, 3, 1, 2, 9, 7 ,6]
w = [6,4,1,3]
ww = w
# w = [2,5,7,0,1,2,7,3,9,5]
# m = [2,5,7,0,1,2,7,3,9,5]
m = [6,4,5,1,3]
mm = m
# n = [2,5,7,0,1,2,7,3,9,5]
n = [6,4,5,1,3]
nn = n

q = insertionSort(x, descending)
c = 0
s = 0

# insertion PLAYGROUND
print("Insert >= x", t, " ->", insertionSort(x, descending))
print("Insert <= y", t, " ->", insertionSort(y, ascending))

# Merge PLAYGROUND
z1 = mergeSort(z, descending)
print("Merge >= z", t, " ->", z1 , mergecomp, mergesub)
print(z1, " ---", finalCheck(z1, descending))
mergecomp = 0

w1 = mergeSort(w, ascending)
print("Merge <= w", ww, " ->", w1 , mergecomp, mergesub)
print(w1, " ---", finalCheck(w1, ascending))
mergecomp = 0

# quickSort PLAYGROUND
quickSort(m, 0, len(m)-1, ">=")
q1b = quicksub
q1a = quickcomp
quicksub = 0
quickcomp = 0

print("\n")

quickSort(n, 0, len(n)-1, "<=")
q2b = quicksub
q2a = quickcomp
quicksub = 0
quickcomp = 0

print("Quick >= m", mm, " ->", m, q1a, q1b)
print("Quick <= n", nn, " ->", n, q2a, q2b)

i = [8,2,4,9,3,6]
ii = i
print("TEST", ii, "-->", insertionSort(i, ascending))


# tow ways to stderr !!!
print("test standart error", file=sys.stderr)
sys.stderr.write("test standart output error\n")

# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n-1)
#
# print(f(4))

# xc = [2,5,7,0,1,2,7,3,9,5]
# print(partitionHoare(xc, 0, len(xc) -1, ascending))
# print("XX", xx)
#
# if __name__ == '__main__':
#     import timeit
#     print("-><-><-><-><-", timeit.timeit("f(5)", setup="from __main__ import f"))
#     print("-><-><-><-><-", timeit.timeit("f(10)", setup="from __main__ import f"))
#     print("-><-><-><-><-", timeit.timeit("f(20)", setup="from __main__ import f"))

# # linear search function
# def linear_search(mylist, find):
#     for x in mylist:
#         if x == find:
#             return True
#     return False
#
# # compute linear search time
# def linear_time():
#     SETUP_CODE = '''
# from __main__ import linear_search
# from random import randint'''
#
#     TEST_CODE = '''
# mylist = [x for x in range(10000)]
# find = randint(0, len(mylist))
# linear_search(mylist, find)
#     '''
#     # timeit.repeat statement
#     times = timeit.repeat(setup = SETUP_CODE,
#                           stmt = TEST_CODE,
#                           repeat = 3,
#                           number = 10000)
#
#     # priniting minimum exec. time
#     print('Linear search time: {}'.format(min(times)))
#
# linear_time()
