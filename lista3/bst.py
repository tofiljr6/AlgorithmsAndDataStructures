import sys
import time
import codecs

comparision = 0


class Node:
    """Interpretation of single node in the binary tree"""
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def inOrder(root):
    """The method prints the tree in in order way"""
    global comparision

    comparision += 1
    if root is not None:
        inOrder(root.left)
        print(root.key, end=" ")
        inOrder(root.right)


def find(node, k):
    """The method finds k value in the tree"""
    global comparision

    comparision += 1
    if node is None or k == node.key:
        return node

    comparision += 1
    if k < node.key:
        return find(node.left, k)
    else:
        return find(node.right, k)


def minimum(node):
    """The method finds min in the tree"""
    global comparision

    comparision += 1
    while node.left is not None:
        comparision += 1
        node = node.left
    return node


def maximum(node):
    """The method finds max in the tree"""
    global comparision

    comparision += 1
    while node.right is not None:
        comparision += 1
        node = node.right
    return node


def succesor(node, case=0, value="a"):
    """The method finds next node from current node value"""
    global comparision

    if case == 1:
        node = find(node, value)

    comparision += 1
    if node.right is not None:
        return minimum(node.right)
    y = node.parent
    while y is not None and node == y.right:
        node = y
        y = y.parent
    return y


def insert(T, z):
    """The method inserts new value to the tree"""
    global comparision

    z = Node(z)
    y = None
    x = T
    comparision += 1
    while x is not None:
        comparision += 1
        y = x
        comparision += 1
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    comparision += 1
    if y is None:
        T = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return T


def transplant(T, u, v):
    """The method is used in delete node in the binary tree"""
    global comparision
    comparision += 1
    if u.parent is None:
        T = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    comparision += 1
    if v is not None:
        v.parent = u.parent


def delete(T, z):
    """The method removes node in the tree"""
    global comparision
    z = find(T, z)
    comparision += 1
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = minimum(z.right)
        comparision += 1
        if y.parent.key != z.key:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y

# # root = None
# # root = insert(root, 50)
# # root = insert(root, 30)
# # root = insert(root, 20)
# # root = insert(root, 40)
# # root = insert(root, 70)
# # root = insert(root, 60)
# # root = insert(root, 80)
# # inOrder(root)
# # print("---")
# # delete(root, 30)
# # inOrder(root)
# # print("\n")
# # print(succesor(root))
#
#
#
#
#
# def doWork():
#     args = sys.argv
#     args = args[1:]
#
#     root = None
#
#     operation = {
#         "insert": 0,
#         "inorder": 0,
#         "delete": 0,
#         "max": 0,
#         "min": 0,
#         "find": 0,
#         "load": 0,
#         "successor": 0
#     }
#     elems = 0
#     delems = 0
#
#     if len(args) == 0:
#         print("No argument")
#     else:
#         if args[0] == "-type":
#             if args[1] == "bst":
#                 n = int(input())
#                 startTime = time.time()
#                 for i in range(n):
#                     command = input()
#                     command = command.split(" ")
#                     operation[command[0]] += 1
#                     if command[0] == "insert":
#                         root = insert(root, prepare(command[1]))
#                         elems += 1
#                     elif command[0] == "inorder":
#                         inOrder(root)
#                         print(" ")
#                     elif command[0] == "delete":
#                         delete(root, command[1])
#                         delems += 1
#                     elif command[0] == "max":
#                         print(maximum(root).key)
#                     elif command[0] == "min":
#                         print(minimum(root).key)
#                     elif command[0] == "find":
#                         x = find(root, command[1])
#                         if x is not None:
#                             print(1)
#                         else:
#                             print(0)
#                     elif command[0] == "load":
#                         print("load", command[1])
#                         # this code fragment works only for small file, otherwise in stackoverflow
#                         # file = open(command[1])
#                         # for f in file:
#                         #     parts = f.split(" ")
#                         #     for part in parts:
#                         #         root = insert(root, prepare(part))
#                         #         elems += 1
#                         with codecs.open(command[1], 'r', encoding="utf-8", errors="ignore") as fdata:
#                             file = fdata.read().split()
#                             for f in file:
#                                 root = insert(root, prepare(f))
#                                 elems += 1
#                     elif command[0] == "successor":
#                         print(succesor(root, 1, "aaa").key)
#                 endTime = time.time()
#                 dt = round(endTime - startTime, 20)
#                 sys.stderr.write("%f \n" % dt)
#         else:
#             print("Unrecognized param")
#
#         for key, value in operation.items():
#             sys.stderr.write("%s \n" % (key + " " + str(value)))
#         sys.stderr.write("MAX NUMBER OF ELEMS %d \n" % elems)
#         sys.stderr.write("CURRENT NUMBER OF ELEMS %d \n" % (elems - delems))
#         sys.stderr.write("COMP: %d \n" % comparision)
#
#
# if __name__ == '__main__':
#     doWork()
#
# # file = open("lotr.txt", "r+")
# # text = file.read().decode(errors='replace')
# # for f in text:
# #     print(f.encode('utf-8').strip())
#
#
# # with codecs.open("lotr.txt", 'r', encoding="utf-8", errors='ignore') as fdata:
# #     print(fdata.read().split())