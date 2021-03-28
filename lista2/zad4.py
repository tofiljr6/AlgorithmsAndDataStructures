# Python implementation of the above approach

c = 0
s = 0


# Function to perform the insertion sort
def insertion_sort(arr, low, n):
    global s, c
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        c += 1
        while j>low and arr[j-1]>val:
            arr[j]= arr[j-1]
            s += 1
            j-= 1
        arr[j]= val
        s += 1

# The following two functions are used
# to perform quicksort on the array.

# Partition function for quicksort
def partition(arr, low, high):
    global s, c
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        s += 1
        if arr[i]<pivot:
            s += 1
            a[i], a[j]= a[j], a[i]

            j+= 1
    s += 1
    a[j], a[high]= a[high], a[j]
    return j

# Function to call the partition function
# and perform quick sort on the array
def quick_sort(arr, low, high):
    if low<high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot + 1, high)
        return arr

# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, low, high):
    while low<high:

        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high-low + 1<10:
            insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)

            # Optimised quicksort which works on
            # the smaller arrays first

            # If the left side of the pivot
            # is less than right, sort left part
            # and move to the right part of the array
            if pivot-low<high-pivot:
                hybrid_quick_sort(arr, low, pivot-1)
                low = pivot + 1
            else:
                # If the right side of pivot is less
                # than left, sort right side and
                # move to the left side
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot-1

# Driver code
import random
import time

file = open("hybrid2.txt", "w")

for q in range(3):
    for kk in range(1, 101):
        a = [random.randint(1, 3000) for i in range(kk * 100)]
        start = time.time()
        hybrid_quick_sort(a, 0, len(a) - 1)
        stop = time.time()
        # print(a)
        r = "HYBRID: " +  str(kk * 100) + " " +  str(s) + " " +str(c) + " " + str(stop-start) + "\n"
        print(r)
        file.write(r)
        s,c = 0, 0

file.close()
