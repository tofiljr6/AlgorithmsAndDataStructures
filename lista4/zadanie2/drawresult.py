from matplotlib import pyplot as plt
import math

x = [8, 250, 1000, 10000]
y = [0.000156640996666666,
     0.0128035942766666,
     0.146181360873333,
     12.26182565688]

z = [ex/4 for ex in x]
y2 = []
for i in range(len(x)):
    c = (x[i] + z[1]) *math.log(z[1], 10)
    wsp = 0.0008
    y2.append(c*wsp)

plt.plot(x, y, label="time")
plt.plot(x, y2, label="O((|V|+|E|)*log(|V|)")
plt.xlabel("Number of vertex")
plt.ylabel("time in ms")
plt.title("time exec dijkstra")
plt.legend()
plt.show()