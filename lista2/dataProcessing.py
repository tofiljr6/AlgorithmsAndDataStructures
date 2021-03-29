import numpy as np
from matplotlib import pyplot as plt
from math import log

file = open('result4.txt', 'r')
file2 = open('hybrid3.txt', 'r')

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
    elif i3 == 3:
        title = "experiment const"
        ylabel = "const in dp"

    return title, xlabel, ylabel


def table(index1, index2, index3):
    xquick = []
    yquick = []
    xmerge = []
    ymerge = []
    xinsert = []
    yinsert = []
    xdp = []
    ydp = []
    xhybrid = []
    yhybrid = []

    xquickfinal = []
    yquickfinal = []
    xmergefinal = []
    ymergefinal = []
    xinsertfinal = []
    yinsertfinal = []
    xdpfinal = []
    ydpfinal = []
    xhybridfinal = []
    yhybridfinal = []

    i = 0
    j = 0
    k = 0
    m = 0
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
                elif index3 == 3:
                    pass
                # print(xquick, yquick)
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
            elif line[0] == "DPivot:":
                xdp.append(float(line[index1]))
                if index3 == 0:
                    ydp.append(float(line[index2]))
                elif index3 == 1 or index3 == 2:
                    ydp.append(float(line[index2])/float(line[index1]))
                elif index3 == 3:
                    pass

                m += 1
                if m % 100 == 0:
                    xdpfinal.append(xdp)
                    ydpfinal.append(ydp)
                    xdp = []
                    ydp = []


    hh = 0
    for l2 in file2:
        l2 = l2.split(" ")
        line = []


        if len(l2) > 1:
            line.append(l2[0])
            line.append(l2[1])
            line.append(l2[2])
            line.append(l2[3])

            if len(l2) > 2:
                tline = l2[4].rsplit("\n")
                line.append(tline[0])

            xhybrid.append(float(line[index1]))
            if index3 == 0:
                yhybrid.append(float(line[index2]))
            elif index3 == 1 or index3 == 2:
                yhybrid.append(float(line[index2])/float(line[index1]))

            hh += 1
            if hh % 100 == 0:
                xhybridfinal.append(xhybrid)
                yhybridfinal.append(yhybrid)
                xhybrid = []
                yhybrid = []

    title, xlabel, ylabel = titleGenerator(index1, index2, index3)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    m = 0

    avgxhybrid = []
    avgyhybrid = []
    xtemp = []
    ytemp = []
    index = 0
    print(xhybridfinal)
    for j in range(100):
        # print(xhybridfinal[0][j], xhybridfinal[1][j], xhybridfinal[2][j])
        sx = 0
        sy = 0

        for zxc in range(len(xhybridfinal)):
            xtemp.append(xhybridfinal[zxc][j])
            ytemp.append(yhybridfinal[zxc][j])

        sx = sum(xtemp)/len(xhybridfinal)
        sy = sum(ytemp)/len(xhybridfinal)

        avgxhybrid.append(sx)
        avgyhybrid.append(sy)

        print(sx, sy)
        xtemp, ytemp = [], []

    plt.plot(avgxhybrid, avgyhybrid, 'r-', label="avg hybrid")

    for i in range(len(xquickfinal)):
        if m == 0:
            plt.plot(xquickfinal[i], yquickfinal[i], 'g-', label="quicksort")
            # plt.plot(xmergefinal[i], ymergefinal[i], 'c-', label="mergesort")
            # plt.plot(xinsertfinal[i], yinsertfinal[i], 'r-', label="insertsort")
            plt.plot(xdpfinal[i], ydpfinal[i], 'm-', label="quicksort - dual pivot")
            # plt.plot(xhybrid, yhybrid, 'k-', label="hybrid")
            plt.plot(xhybridfinal[i], yhybridfinal[i], 'k-', label="hybrid")
            m += 1

    # xnlogn = np.linspace(100, 10000, 100)
    # tmp = float(xnlogn/1000000)
    # ynlogn = xnlogn * np.log(xnlogn)
    # ynlogn = (xnlogn * np.log(xnlogn))/1000000
    # plt.plot(xnlogn, ynlogn, 'y-', label="nlogn")

    # xx2 = np.arange(100, 10000)
    # yy2 = xx2 ** 2
    # plt.plot(xx2, yy2, 'r--', label="x^2")


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
# table(1,3,2)

table(1,4,0)




file.close()
file2.close()



# table(1,2, 2)
