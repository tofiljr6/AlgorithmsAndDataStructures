from math import floor

def countPart(A, low, high):
    i = low + 1
    k = high -1
    j = i
    d = 0

    leftPivot = A[low]
    rightPivot = A[high]

    while j <= k:
        if d > 0:
            if A[j] < leftPivot:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1
                d += 1
            else:
                if A[j] < rightPivot:
                    j += 1
                else:
                    A[j], A[k] = A[k], A[j]
                    k -= 1
                    d -= 1
        else:
            while A[k] > rightPivot:
                k -= 1
                d -= 1
            if j <= k:
                if A[k] < leftPivot:
                    A[k], A[j], A[i] = A[j], A[i], A[k]
                    i += 1
                    d += 1
                else:
                    A[j], A[k] = A[k], A[j]
                j += 1
    A[low], A[i-1] = A[i-1], A[low]
    A[high], A[k+1] = A[k+1], A[high]
    return i -1, k + 1


def sortAsc(A, low, high):
    if low < high:
        if A[low] > A[high]:
            A[low], A[high] = A[high], A[low]

        p, q = countPart(A, low, high)

        sortAsc(A, low, p -1)
        sortAsc(A, p+1, q-1)
        sortAsc(A, q+1, high)

# x = [4,2,8,6,9,1,3,7,5]
# x = [i * 10 for i in x]
x = ['Mateusz', 'Piotrek', 'Adam', 'Abcka', 'Abc']
print(x)

sortAsc(x, 0, len(x) - 1)
print(x)

# y = countPart(x, 0, len(x) - 1)
# print(x, y)


# def countPart2(A, low, high):
#     i = low + 1
#     k = high -1
#     j = i
#     d = 0
#
#     leftPivot = A[low]
#     rightPivot = A[high]
#
#     while j <= k:
#         if d > 0:
#             if A[j] > leftPivot:
#                 A[i], A[j] = A[j], A[i]
#                 i += 1
#                 j += 1
#                 d += 1
#             else:
#                 if A[j] > rightPivot:
#                     j += 1
#                 else:
#                     A[j], A[k] = A[k], A[j]
#                     k -= 1
#                     d -= 1
#         else:
#             while A[k] < rightPivot:
#                 k -= 1
#                 d -= 1
#             if j <= k:
#                 if A[k] > leftPivot:
#                     A[k], A[j], A[i] = A[j], A[i], A[k]
#                     i += 1
#                     d += 1
#                 else:
#                     A[j], A[k] = A[k], A[j]
#                 j += 1
#     A[low], A[i-1] = A[i-1], A[low]
#     A[high], A[k+1] = A[k+1], A[high]
#     return i -1, k + 1
#
#
# def sortAsc2(A, low, high):
#     if low < high:
#         if A[low] < A[high]:
#             A[low], A[high] = A[high], A[low]
#
#         p, q = countPart(A, low, high)
#
#         sortAsc(A, low, p -1)
#         sortAsc(A, p+1, q-1)
#         sortAsc(A, q+1, high)
#
# x = [4,2,8,6,9,1,3,7,5]
# x = [i * 10 for i in x]
# print(x)
# sortAsc2(x, 0, len(x) - 1)
# print(x)
#
