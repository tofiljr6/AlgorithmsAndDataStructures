import numpy as np
from matplotlib import pyplot as plt
from math import log

fileDPQuickSort = open('testDPQuickSort3.txt', 'r')


def preperaLine(l):
    line = []
    # space line '\n' - ignored
    if len(l) > 1:
        line.append(l[0])
        line.append(l[1])
        line.append(l[2])
        line.append(l[3])

    # number of seconds - rsplited ....\n
    if len(l) > 2:
        tline = l[4].rsplit("\n")
        line.append(tline[0])

    return line


def collectData(l):
    pass

xdp = []
ydp = []
xdpfinal = []
ydpfinal = []
xavgdp = []
yavgdp = []
sample = 0;
K = 4

for f in fileDPQuickSort:
    # obróbka danych
    l = f.split(' ')

    if sample % 100 == 0:
        if len(xdp) != 0:
            xdpfinal.append(xdp)
            ydpfinal.append(ydp)
            xdp = []
            ydp = []

    line = preperaLine(l)

    if len(line) > 0:
        if line[0] == 'DPivot:':
            xdp.append(int(line[1]))
            ydp.append(float(line[4]))
            sample += 1


# for i in range(len(xdpfinal)):
#     plt.plot(xdpfinal[i], ydpfinal[i], 'y-')
    # plt.plot(xdpfinal[1], ydpfinal[1], 'g-', label="Dual pivot")
    # plt.plot(xdpfinal[2], ydpfinal[2], 'b-', label="Dual pivot")
    # plt.plot(xdpfinal[3], ydpfinal[3], 'r-', label="Dual pivot")

for i in range(len(xdpfinal[0])): #numer of samples
    # print(i)
    xs = 0
    ys = 0
    for k in range(K):
        xs += float(xdpfinal[k][i])
        ys += float(ydpfinal[k][i])

    xs = xs / K
    ys = ys / K

    xavgdp.append(xs)
    yavgdp.append(ys)

# dual pivot first sample
# plt.plot(xdpfinal[0], ydpfinal[0], 'm-', label="Dual pivot sample 1")
# avg dual pivot
plt.plot(xavgdp, yavgdp, 'c-', label="Dual pivot avg")
# n log n
xnlogn = np.linspace(100, 10000, 100)
ynlogn = (xnlogn * np.log(xnlogn))/1000000
plt.plot(xnlogn, ynlogn, 'b-', label="nlogn avg case")
# n
xn = np.linspace(100, 10000, 100)
yn = xn/1000000
plt.plot(xn, yn, '-g', label="n - best case")
# n^2
# yn = (xn ** 2)/1000000
# plt.plot(xn, yn, 'r', label="n^2 - worst case")

plt.title("Dual Pivot")
plt.xlabel("Number of elements")
plt.ylabel("Time exec")
plt.legend()
plt.show()

fileDPQuickSort.close()
