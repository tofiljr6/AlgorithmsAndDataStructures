import numpy as np
from matplotlib import pyplot as plt
from math import log

file = open('result2.txt', 'r')

xnlogn = np.linspace(100, 10000, 100)
ynlogn = np.log2(xnlogn) * xnlogn
plt.clf()
# plt.plot(xnlogn, ynlogn, 'm--', label="nlogn")

xx2 = np.arange(100, 10000)
yy2 = 0.45 * xx2 ** 2
# plt.plot(xx2, yy2, 'c--', label="x^2")

def titleGenerator(i1, i2, i3):
    title = ""
    xlabel = ""
    ylabel = ""
    if i1 == 1:
        title += "Elements in array against "
        xlabel = "elements in array"

    if i2 == 2:
        title += "comparistion"
        ylabel = "number of comparistioni"
    elif i2 == 3:
        title += "substitution"
        ylabel = "number of substitution"
    elif i2 == 4:
        title += "time of execution"
        ylabel = "time of execution"

    if i3 == 1:
        title = "c/n against n"
        ylabel = "c/n"
    elif i3 == 2:
        title = "s/n against n"
        ylabel = "s/n"

    return title, xlabel, ylabel


def table(index1, index2, index3):
    xquick = []
    yquick = []
    xmerge = []
    ymerge = []
    xinsert = []
    yinsert = []
    xquickfinal = []
    yquickfinal = []
    xmergefinal = []
    ymergefinal = []
    xinsertfinal = []
    yinsertfinal = []

    i = 0
    j = 0
    k = 0
    # global xquickfinal, yquickfinal
    for l in file:
        l = l.split(" ")
        line = []

        if len(l) > 1:
            line.append(l[0])
            line.append(l[1])
            line.append(l[2])
            line.append(l[3])

            if len(l) > 2:
                tline = l[4].rsplit("\n")
                line.append(tline[0])


            # print("SPLITED:", line)
            if line[0] == "QUICK:":
                xquick.append(float(line[index1]))
                if index3 == 0:
                    yquick.append(float(line[index2]))
                elif index3 == 1 or index3 == 2:
                    yquick.append(float(line[index2])/float(line[index1]))
                print(xquick, yquick)
                i += 1
                if i % 100 == 0:
                    xquickfinal.append(xquick)
                    yquickfinal.append(yquick)
                    xquick = []
                    yquick = []
            elif line[0] == "MERGE:":
                xmerge.append(float(line[index1]))
                if index3 == 0:
                    ymerge.append(float(line[index2]))
                elif index3 == 1 or index3 == 2:
                    ymerge.append(float(line[index2])/float(line[index1]))
                j += 1
                if j % 100 == 0:
                    xmergefinal.append(xmerge)
                    ymergefinal.append(ymerge)
                    xmerge = []
                    ymerge = []
            elif line[0] == "INSERT:":
                xinsert.append(float(line[index1]))
                if index3 == 0:
                    yinsert.append(float(line[index2]))
                elif index3 == 1 or index3 == 2:
                    yinsert.append(float(line[index2])/float(line[index1]))
                k += 1
                if k % 100 == 0:
                    xinsertfinal.append(xinsert)
                    yinsertfinal.append(yinsert)
                    xinsert = []
                    yinsert = []

    title, xlabel, ylabel = titleGenerator(index1, index2, index3)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    m = 0

    for i in range(len(xquickfinal)):
        if m == 0:
            plt.plot(xquickfinal[i], yquickfinal[i], 'g-', label="quicksort")
            plt.plot(xmergefinal[i], ymergefinal[i], 'y-', label="mergesort")
            plt.plot(xinsertfinal[i], yinsertfinal[i], 'r-', label="insertsort")
            m += 1

    plt.legend()
    plt.show()


# avg number of comparistion againts elements n
# table(1,2,0)

# avg number of substitution againts elements n
# table(1,3,0)

# time execution againts elements n
# table(1,4,0)

# c/n agains n
# table(1,2,1)

# s/n againts n
table(1,3,2)








# table(1,2, 2)
