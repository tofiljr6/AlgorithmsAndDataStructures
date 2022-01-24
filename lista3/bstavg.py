import time
import bst
import codecs
import random


def prepare(s):
    """The method preapres string to insert in the tree [a-zA-Z]"""
    result = ""
    if s[0].isalpha():
        result += s[0]
    result += s[1:len(s) - 1]
    if s[len(s) - 1].isalpha() and len(s) > 1:
        result += s[len(s) - 1]
    return result


# with codecs.open("aspell_wordlist.txt", "r", encoding="utf-8", errors="ignore") as fdata:
#     file = fdata.read().split()
# random.shuffle(file)

with codecs.open("lotr.txt", "r", encoding="utf-8", errors="ignore") as fdata:
    file = fdata.read().split()

# aspell - max 1100
# lotr - 10100
for i in range(100, 10100, 100):
    root = None
    inserttime = 0
    deletetime = 0
    findtime = 0
    mintime = 0
    maxtime = 0
    succesortime = 0
    for k in range(i):
        starttime = time.time()
        root = bst.insert(root, prepare(file[k]))
        endtime = time.time()
        inserttime += round(endtime - starttime, 20)

    # element we will find in the tree
    first = prepare(file[0])
    last = prepare(file[i - 1])
    x = random.randint(1, i - 2)
    ra = prepare(file[x])

    # minimum
    starttime = time.time()
    bst.minimum(root)
    endtime = time.time()
    mintime = round(endtime - starttime, 20)

    # maximum
    starttime = time.time()
    bst.maximum(root)
    endtime = time.time()
    maxtime = round(endtime - starttime, 20)

    # find random value in the tree
    starttime = time.time()
    bst.find(root, first)
    endtime = time.time()
    findtime += round(endtime - starttime, 20)

    # successor
    starttime = time.time()
    bst.succesor(root, ra)
    endtime = time.time()
    succesortime += round(endtime - starttime, 20)

    # delete element
    starttime = time.time()
    bst.delete(root, ra)
    endtime = time.time()
    deletetime += round(endtime - starttime, 20)

    print(i, inserttime / i, deletetime, findtime, mintime, maxtime, succesortime)
    # print("\n")
