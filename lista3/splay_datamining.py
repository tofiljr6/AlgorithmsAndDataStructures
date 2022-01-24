import time
import random
import splay
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


with codecs.open("aspell_wordlist.txt", "r", encoding="utf-8", errors="ignore") as fdata:
    file = fdata.read().split()
#
# random.shuffle(file)

# with codecs.open("lotr.txt", "r", encoding="utf-8", errors="ignore") as fdata:
#     file = fdata.read().split()

for i in range(100, 10100, 100):
    arr = [0,0,0,0]
    tree = splay.splayTree()
    avgtime = 0
    for k in range(i):
        # print(k, prepare(file[k]))
        tree.insert(prepare(file[k]))
        endtime = time.time()
    tree.comparision = 0
    tree.find(file[0])
    arr[0] = tree.comparision

    tree.comparision = 0
    tree.find(file[i//2])
    arr[1] = tree.comparision

    tree.comparision = 0
    tree.find(file[i-1])
    arr[2] = tree.comparision

    tree.comparision = 0
    for k in range(10):
        tree.find(file[random.randint(1, i-1)])
        arr[3] = tree.comparision
    tree.comparision = 0

    print(i, arr[0], arr[1], arr[2], arr[3]/10)

