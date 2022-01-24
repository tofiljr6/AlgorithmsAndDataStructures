from matplotlib import pyplot as plt
from math import log2

bstsorted = open("./data2/bst_sorted.txt")
bstshuffle = open("./data2/bst_shuffle.txt")
bstlotr = open("./data2/bst_lotr.txt")

rbtsorted = open("./data2/rbt_sorted.txt")
rbtshuffle = open("./data2/rbt_shuffle.txt")
rbtlotr = open("./data2/rbt_lotr.txt")

splaysorted = open("./data2/splay_sorted.txt")
splayshufle = open("./data2/splay_shuffle.txt")
splaylotr = open("./data2/splay_lotr.txt")

files = [bstsorted, bstshuffle, bstlotr]


def divide(file):
    result = []
    for f in file:
        f = f.split(" ")
        f[0] = int(f[0])
        f[1] = float(f[1])
        f[2] = float(f[2])
        f[3] = float(f[3])
        f[4] = float(f[4].rsplit("\n")[0])
        result.append(f)
    return result

z = divide(splaylotr)
# print(z)

x = [elem[0] for elem in z]
small = [elem[1] for elem in z]
mid = [elem[2] for elem in z]
big = [elem[3] for elem in z]
rad = [elem[4] for elem in z]

plt.title("liczba porównań w splay dla lotr")
plt.plot(x, small, label="dolne")
plt.plot(x, mid, label="polowa")
plt.plot(x, big, label="górne")
plt.plot(x, rad, label="random")

plt.legend()
plt.show()