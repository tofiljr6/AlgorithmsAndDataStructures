from matplotlib import pyplot as plt
from math import log2

bstsorted = open("./data/bst_avg_operation_posortowany.txt")
rbtsorted = open("./data/rbt_avg_operation_posortowany.txt")
splaysorted = open("./data/splay_avg_operation_posortowany.txt")

bstshuffle = open("./data/bst_avg_operation_shuffle.txt")
rbtshuffle = open("./data/rbt_avg_operation_shuffle.txt")
splayshuffle = open("./data/splay_avg_operation_shuffle.txt")

files = [bstsorted, rbtsorted, splaysorted]
files = [bstshuffle, rbtshuffle, splayshuffle]
labels = ["bst", "rbt", "splay"]


def divide(file):
    result = []
    for f in file:
        f = f.split(" ")
        f[0] = int(f[0])
        f[1] = float(f[1])
        f[2] = float(f[2])
        f[3] = float(f[3])
        f[4] = float(f[4])
        f[5] = float(f[5])
        f[6] = float(f[6].rsplit("\n")[0])
        result.append(f)
    return result

# index = 0
# for f in files[0]:
#     # z = divide(f.split(" "))
#     # print(z)
#     print(f)
#     z = divide(files[0])
#     print(z)

    # x = [elem[0] for elem in z]
    # insert = [elem[0] for elem in z]
    # delete = [elem[0] for elem in z]
    # find = [elem[0] for elem in z]
    # mint = [elem[0] for elem in z]
    # maxt = [elem[0] for elem in z]
    # suc = [elem[0] for elem in z]
    #
    # plt.title("Insert time")
    # plt.plot(x, insert, label=labels[index])
    # index += 1

# plt.legend()
# plt.show()

index = 0
for file in files:
    z = divide(file)
    print(z)

    x = [elem[0] for elem in z]
    insert = [elem[1] for elem in z]
    delete = [elem[2] for elem in z]
    find = [elem[3] for elem in z]
    mint = [elem[4] for elem in z]
    maxt = [elem[5] for elem in z]
    suc = [elem[6] for elem in z]
    plt.title("Insert time")
    plt.plot(x, find, label=labels[index])
    index += 1

plt.legend()
plt.show()