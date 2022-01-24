import codecs
import sys
import time

import bst
import rbt2
import splay


def prepare(s):
    """The method preapres string to insert in the tree [a-zA-Z]"""
    result = ""
    for letter in s:
        if letter.isalpha():
            result += letter

    return result


def doWork():
    args = sys.argv
    args = args[1:]

    root = None

    operation = {
        "insert": 0,
        "inorder": 0,
        "delete": 0,
        "max": 0,
        "min": 0,
        "find": 0,
        "load": 0,
        "successor": 0
    }
    elems = 0
    delems = 0

    if len(args) == 0:
        print("No argument")
    else:
        if args[0] == "-type":
            if args[1] == "bst":
                n = int(input())
                startTime = time.time()
                for i in range(n):
                    command = input()
                    command = command.split(" ")
                    operation[command[0]] += 1
                    if command[0] == "insert":
                        root = bst.insert(root, prepare(command[1]))
                        elems += 1
                    elif command[0] == "inorder":
                        bst.inOrder(root)
                        print(" ")
                    elif command[0] == "delete":
                        bst.delete(root, command[1])
                        delems += 1
                    elif command[0] == "max":
                        print(bst.maximum(root).key)
                    elif command[0] == "min":
                        print(bst.minimum(root).key)
                    elif command[0] == "find":
                        x = bst.find(root, command[1])
                        if x is not None:
                            print(1)
                        else:
                            print(0)
                    elif command[0] == "load":
                        print("load", command[1])
                        # this code fragment works only for small file, otherwise in stackoverflow
                        # file = open(command[1])
                        # for f in file:
                        #     parts = f.split(" ")
                        #     for part in parts:
                        #         root = insert(root, prepare(part))
                        #         elems += 1
                        with codecs.open(command[1], 'r', encoding="utf-8", errors="ignore") as fdata:
                            file = fdata.read().split()
                            for f in file:
                                root = bst.insert(root, prepare(f))
                                elems += 1
                    elif command[0] == "successor":
                        print(bst.succesor(root, 1, "aaa").key)
                endTime = time.time()
                dt = round(endTime - startTime, 20)
                sys.stderr.write("%f \n" % dt)
                sys.stderr.write("COMP: %d \n" % bst.comparision)
            if args[1] == "rbt":
                rbt = rbt2.RedBlackTree()
                n = int(input())
                startTime = time.time()
                for i in range(n):
                    command = input()
                    command = command.split(" ")
                    operation[command[0]] += 1
                    if command[0] == "insert":
                        rbt.insert(prepare(command[1]))
                        elems += 1
                    elif command[0] == "inorder":
                        # rbt.inorder()
                        rbt.prettyPrinter()
                    elif command[0] == "delete":
                        rbt.delete(command[1])
                        delems += 1
                    elif command[0] == "max":
                        print(rbt.max())
                    elif command[0] == "min":
                        print(rbt.min())
                    elif command[0] == "find":
                        print(rbt.find(command[1]))
                    elif command[0] == "succesor":
                        print(rbt.successor(command[1]))
                    elif command[0] == "load":
                        with codecs.open(command[1], 'r', encoding="utf-8", errors="ignore") as fdata:
                            file = fdata.read().split()
                            for f in file:
                                rbt.insert(prepare(f))
                                elems += 1
                endTime = time.time()
                dt = round(endTime - startTime, 20)
                sys.stderr.write("%f \n" % dt)
                sys.stderr.write("COMP: %d \n" % rbt.getComparision())
            if args[1] == "splay":
                spl = splay.splayTree()
                n = int(input())
                startTime = time.time()
                for i in range(n):
                    command = input()
                    command = command.split(" ")
                    operation[command[0]] += 1
                    if command[0] == "insert":
                        spl.insert(prepare(command[1]))
                        elems += 1
                    elif command[0] == "inorder":
                        spl.inorder()
                        # spl.pretty_print()
                    elif command[0] == "delete":
                        spl.delete(command[1])
                        delems += 1
                    elif command[0] == "max":
                        print(spl.max())
                    elif command[0] == "min":
                        print(spl.min())
                    elif command[0] == "find":
                        print(spl.find(command[1]))
                    elif command[0] == "succesor":
                        print(spl.successor(command[1]))
                    elif command[0] == "load":
                        with codecs.open(command[1], 'r', encoding="utf-8", errors="ignore") as fdata:
                            file = fdata.read().split()
                            for f in file:
                                spl.insert(prepare(f))
                                elems += 1
                endTime = time.time()
                dt = round(endTime - startTime, 20)
                sys.stderr.write("%f \n" % dt)
                sys.stderr.write("COMP: %d \n" % spl.getComparision())
        else:
            print("Unrecognized param")

        for key, value in operation.items():
            sys.stderr.write("%s \n" % (key + " " + str(value)))
        sys.stderr.write("MAX NUMBER OF ELEMS %d \n" % elems)
        sys.stderr.write("CURRENT NUMBER OF ELEMS %d \n" % (elems - delems))



if __name__ == '__main__':
    doWork()