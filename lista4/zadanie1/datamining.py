from queue import *
import random
import copy

SIZE = 5100  # 000000

value = [random.randint(0, 1000) for i in range(SIZE)]
prior = [random.randint(1, 1000) for i in range(SIZE)]
x = [i for i in range(SIZE)]
datac = []
datas = []
d = []

for w in range(100, SIZE, 100):
    q = Queue()
    for i in range(w):
        q.insert(value[i], prior[i])

    q.reset()
    nrtest = 15
    c = 0
    s = 0
    for i in range(nrtest):
        qq = copy.deepcopy(q)
        # qq.insert(random.randint(1,10), 1100)
        # qq.priority(value[random.randint(0, SIZE)], 12000)
        qq.pop()
        data = qq.get()
        c += data[0]
        s += data[1]

    print(w, c/nrtest, s/nrtest)
    datac.append(c/nrtest)
    datas.append(s/nrtest)

