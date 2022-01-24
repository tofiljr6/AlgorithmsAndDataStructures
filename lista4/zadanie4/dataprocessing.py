from matplotlib import pyplot as plt

srw = [
    (10.1, 37.9, 11.1, 3.639459609985352e-05),
    (245.15, 855.8, 246.15, 0.000394904613494873),
    (3289.1, 11511.25, 3290.1, 0.011671924591064453)
]

g = [
    (4, 14, 5, 2.8133392333984375e-05),
    (49, 149, 50, 0.00044226646423339844),
    (499, 1497, 500, 0.04248809814453125)
]

k = [
    (53, 22, 9, 0.0004458427429199219),
    (5048, 291, 99, 0.04467320442199707),
    (500498, 2991, 999, 6.682507038116455)
]

p = [
    (53, 22, 9, 9.894371032714844e-05),
    (5048, 291, 99, 0.0032968521118164062),
    (500498, 2991, 999, 0.32451796531677246)
]

x = [
    5,
    50,
    500
]

# t = 0 -> kroki
# t = 1 -> łaczny koszt trasy
# t = 2 -> zyżyta dodatkowa pamięc
# t = 3 -> czas działania algorytmu

t = 3
srwfinal = [s[t] for s in srw]
gfinal = [s[t] for s in g]
kfinal = [s[t] for s in k]
pfinal = [s[t] for s in p]

plt.plot(x, srwfinal, label="srw")
plt.plot(x, gfinal, label="greedy")
plt.plot(x, kfinal, label="kruskal")
plt.plot(x, pfinal, label="prim")
plt.legend()

if t == 0:
    plt.title("Kroki")
elif t == 1:
    plt.title("Koszt trasy")
elif t == 2:
    plt.title("zyżyta dodatkowa pamieć")
elif t == 3:
    plt.title("czas działania programu")

plt.show()



