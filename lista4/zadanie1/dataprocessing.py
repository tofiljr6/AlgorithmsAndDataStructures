from matplotlib import pyplot as plt

phigh = open("data/phigh_insert.txt")
pmid = open("data/pmid_insert.txt")
plow = open("data/plow_insert.txt")
comp_pop = open("data/popcomplexity.txt")
comp_priority = open("data/prioritycomplexity.txt")

# files = [phigh, pmid, plow]
files = [comp_priority, comp_pop]

xaxis = []
caxis = []
saxis = []


for file in files:
    xa, ca, sa = [], [], []
    for f in file:
        f = f.split(" ")
        x = int(f[0])
        c = float(f[1])
        s = float(f[2].rsplit("\n")[0])

        xa.append(x)
        ca.append(c)
        sa.append(s)
    xaxis.append(xa)
    caxis.append(ca)
    saxis.append(sa)
    print(xaxis)

plt.title("Substitution")
plt.plot(xaxis[0], caxis[0], label="prority")
plt.plot(xaxis[1], caxis[1], label="pop")
# plt.plot(xaxis[2], saxis[2], label="p low")
plt.legend()
plt.show()