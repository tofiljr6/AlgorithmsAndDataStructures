import time
import random
import rbt2
import codecs


def prepare(s):
    """The method preapres string to insert in the tree [a-zA-Z]"""
    result = ""
    if s[0].isalpha():
        result += s[0]
    result += s[1:len(s)-1]
    if s[len(s)-1].isalpha() and len(s) > 1:
        result += s[len(s)-1]
    return result


# with codecs.open("aspell_wordlist.txt", "r", encoding="utf-8", errors="ignore") as fdata:
#     file = fdata.read().split()
#
# random.shuffle(file)
#
with codecs.open("lotr.txt", "r", encoding="utf-8", errors="ignore") as fdata:
    file = fdata.read().split()

for i in range(100, 10100, 100):
    arr = [0,0,0,0]
    tree = rbt2.RedBlackTree()
    avgtime = 0
    for k in range(10 * i):
        # print(k, prepare(file[k]))
        root = tree.insert(prepare(file[k]))
        endtime = time.time()

    first = prepare(file[0])
    last = prepare(file[i-1])
    mid = prepare(file[i//2])

    tree.comparision = 0
    tree.find(first)
    arr[0] = tree.comparision
    tree.comparision = 0

    tree.find(mid)
    arr[1] = tree.comparision
    tree.comparision = 0

    tree.find(last)
    arr[2] = tree.comparision
    tree.comparision = 0

    for k in range(10):
        x = prepare(file[random.randint(1, i-1)])
        tree.comparision = 0
        tree.find(x)
        arr[3] += tree.comparision
        tree.comparision = 0

    print(i, arr[0], arr[1], arr[2], int(arr[3]/10))