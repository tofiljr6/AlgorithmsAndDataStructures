from math import floor

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
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and compare(key, A[i], dec):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

def mergeSort(A, dec):
    """ The method sorts A - array in merge sort way.
        A method returns array in 'dec' order.
    """
    if len(A) > 1:
        return merge(mergeSort(A[:floor(len(A)/2)], dec),
                     mergeSort(A[floor((len(A)/2)):], dec), dec)
    else:
        return A

def merge(C, D, dec):
    """ The method merge two sorted arrays keeping them still sorted.
        A method helps in main algoritm mergeSort.
    """
    if len(C) == 0:
        return D
    if len(D) == 0:
        return C
    if compare(C[0], D[0], dec):
        return C[0:1] + merge(C[1:], D, dec)
    else:
        return D[0:1] + merge(C, D[1:], dec)


def quickSort(A, p, r, dec):
    """ The method sorts A - array in quick sort way QS(A,0,len(A)-1).
    """
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

    while True:
        while True:
            i += 1
            if compare(pivot, A[i], dec):
                break

        while True:
            j -= 1
            if compare(A[j], pivot, dec):
                break

        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]

ascending = "<="
descending = ">="

t = [2,5,7,0,1,2,7,3,9,5]
x = [2,5,7,0,1,2,7,3,9,5]
y = [2,5,7,0,1,2,7,3,9,5]
z = [2,5,7,0,1,2,7,3,9,5]
w = [2,5,7,0,1,2,7,3,9,5]
m = [2,5,7,0,1,2,7,3,9,5]
n = [2,5,7,0,1,2,7,3,9,5]

print("Insert >= x", t, " ->", insertionSort(x, descending))
print("Insert <= y", t, " ->", insertionSort(y, ascending))
print("Merge >= z", t, " ->", mergeSort(z, descending))
print("Merge <= w", t, " ->", mergeSort(w, ascending))
quickSort(m, 0, len(m)-1, ">=")
quickSort(n, 0, len(n)-1, "<=")
print("Quick >= m", t, " ->", m)
print("Quick <= n", t, " ->", n)
