import random
import time
import copy
import sys
import math


class Node:
    def __init__(self, value, p):
        self.value = value
        self.p = p

    def __str__(self):
        return "{" + str(self.value) + ":" + str(self.p) + "}"

class Queue:
    def __init__(self):
        self.A = []
        self.c = 0  # comparision
        self.s = 0  # substitution

    @staticmethod
    def parent(i):
        """Returns the parent of i - node"""
        return max(0, (i - 1) // 2)

    @staticmethod
    def left(i):
        """Returns the left children of i - node"""
        return 2 * i + 1

    @staticmethod
    def right(i):
        """Returns the right children of i - node"""
        return 2 * i + 2

    def smallest(self, i):
        """
        The method check avaiable parend and children. Add them to arrays (values and indexs).
        Then return the minimum node of the minimal piority.

        :param i: the index of node we will check
        :return: return the index of node with the minimal priority
        """
        a = []  # tablica indeksów
        b = []  # tablica wartości - p
        c = []  # tablcia wartości - value
        try:
            c.append(self.A[i].value)
            b.append(self.A[i].p)
            a.append(i)
        except IndexError:
            pass

        try:
            c.append(self.A[self.left(i)].value)
            b.append(self.A[self.left(i)].p)
            a.append(self.left(i))
        except IndexError:
            pass

        try:
            c.append(self.A[self.right(i)].value)
            b.append(self.A[self.right(i)].p)
            a.append(self.right(i))
        except IndexError:
            pass

        if len(b) == 0:
            return 0

        # if b.count(min(b)) > 1:  # jeżeli piorytety są takie same, to wg wartości
        #     return a[c.index(min(c))]

        return a[b.index(min(b))]

    def insert(self, key, p):
        """
        The method inserts the new node with key value, and with p priority.
        :param key: key of inserted node
        :param p: priority of inserted node
        """
        x = Node(key, p)
        self.A.append(x)
        i = len(self.A) - 1

        self.c += 1

        while i > 0 and self.A[self.parent(i)].p > p:
            self.c += 1
            self.s += 1
            self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
            i = self.parent(i)

    def print(self):
        """ The method prints all nodes in the array

            The complexity of this is O(n), where n is a number of elements
        """
        for i in self.A:
            print(i, end=" ")
        print("")

    def empty(self):
        """ The method return 1 if the array is empty, 0 in the otherwise"""
        return 1 if len(self.A) == 0 else 0

    def top(self):
        """ The method return only max node with the maximal priority"""
        return self.A[0]

    def pop(self):
        """ The method returns and deletes the max node with the maximal priority"""
        self.c += 1

        if len(self.A) < 1:
            return "heap underflow"
        m = self.A[0]

        self.s += 1

        self.A[0] = self.A[len(self.A) - 1]
        self.A.pop()
        self.heapify(0)
        return m

    def heapify(self, i):
        """
        The method heaps the heap and repair priotiry in the nodes

        :param i: index of node we will repair
        """
        smallest = self.smallest(i)
        self.c += 1
        if smallest != i:
            self.s += 1
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.heapify(smallest)

    def priority(self, x, bigger_p):
        """ If we want to increase the priority of node with x - value, and this
            value doesn't exist in array, we do nothing. O(n)

            Otherwise, for all node with value x we increases priority and do heapifu
            Complexity:
            Let m : all node with we change
                    For each m_i we do heapify -> O(lgm)
            Therefor:
                    The complexity of increase key for all x - values: O (n * lgn)
        """
        for i in range(len(self.A)):
            self.c += 1
            if self.A[i].value == x: # and self.A[i].p < bigger_p:
                self.s += 1
                self.A[i].p = bigger_p
                self.heapify(i)

    def reset(self):
        self.c = 0
        self.s = 0

    def get(self):
        return self.c, self.s

    def decreasekey(self, x, smaller_key):
        for i in range(len(self.A)):
            if self.A[i].value == x:
                self.A[i].p = smaller_key
                self.heapify(self.parent(i))
        # if len(self.A) > 2:
        #     self.A[0], self.A[1] = self.A[1], self.A[0]

    def inner(self, x):
        for i in self.A:
            if i.value == x:
                return True
        return False

class K:
    def __init__(self, V):
        self.V = [i for i in range(V)]
        self.E = []

    def addEdge(self, u, v, w):
        self.E.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """
        The method merges two sets
        """
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        """
        The method uses Kruskal's algoriithm to find MST (Minimum Spanning Tree) using Heap
        """
        result = []

        Q = Queue()
        for e in self.E:
            u, v, w = e
            Q.insert([u, v], w)

        parent = []
        rank = []

        for node in self.V:
            parent.append(node)
            rank.append(0)

        while not Q.empty():
            qq = Q.pop()
            u, v = qq.value
            w = qq.p
            if self.find(parent, u) != self.find(parent, v):
                result.append([u, v, w])
                self.union(parent, rank, self.find(parent, u), self.find(parent, v))

        sumMST = 0
        # for u, v, w in result:
        #     sumMST += w
        #     print("{} {} {}".format(min(u, v), max(u, v), w))
        # print("{}".format(sumMST))
        return result

class P:
    def __init__(self, V):
        self.V = [i for i in range(V)]
        self.E = [[0.0 for i in range(len(self.V))] for j in range(len(self.V))]

    def addEdge(self, u, v, w):
        self.E[u][v] = w
        self.E[v][u] = w

    def prim(self):
        key = [math.inf] * len(self.V)
        parent = [None] * len(self.V)
        key[0] = 0
        mstSet = [False] * len(self.V)

        parent[0] = -1
        for cout in range(len(self.V)):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(len(self.V)):
                if 0 < self.E[u][v] < key[v] and mstSet[v] == False:
                    key[v] = self.E[u][v]
                    parent[v] = u

        sumMST = 0

        verresult = []

        for i in range(1, len(self.V)):
            u = parent[i]
            v = i
            sumMST += self.E[i][parent[i]]
            # print("{} {} {}".format(min(u, v), max(u, v), self.E[i][parent[i]] ))

            verresult.append([min(u, v), max(u, v), self.E[i][parent[i]] ])

        # print(sumMST)
        return verresult

    def minKey(self, key, mstSet):
        min = math.inf

        for v in range(len(self.V)):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

class Graph:
    def __init__(self, V):
        self.V = [i for i in range(V)]
        self.E = [[0.0 for i in range(V)] for i in range(V)]
        self.S = []
        self.kroki = 0   # k - kroki  dodatkowa pamięć,

    def generate(self):
        """
        The method generates the weight of edges with traingle rule.
        """
        for j in range(len(self.V)-2):
            for i in range(len(self.V) - 2):
                t = False
                while not t:
                    tt = 0
                    v = len(self.V)
                    a = random.randint(3, 4) if self.E[0+j][1+i] == 0.0 else self.E[0+j][1+i]
                    b = random.randint(3, 4) if self.E[(1+i+j)%v][2+i] == 0.0 else self.E[(1+i+j)%v][2+i]
                    c = random.randint(3, 4) if self.E[0+j][2+i] == 0.0 else self.E[0+j][2+i]

                    x = [a, b, c]
                    x.sort()
                    # print(x)
                    for elem in range(len(x)):
                        if x[elem % 3] + x[(elem+1) % 3] > x[(elem +2) % 3]:
                            tt += 1
                    if tt == 3:
                        t = True
                        self.E[0+j][1+i] = x[x.index(a)]
                        self.E[1+i][0+j] = x[x.index(a)]

                        self.E[(1+i+j)%v][2+i] = x[x.index(b)]
                        self.E[2+i][(1+i+j)%v] = x[x.index(b)]

                        self.E[0+j][2+i] = x[x.index(c)]
                        self.E[2+i][0+j] = x[x.index(c)]
        for i in range(len(self.V)):
            self.E[i][i] = 0

    def addEdge(self, u, v, w):
        """
        The method adds to the graph new edge with weight
        :param u: start vertex
        :param v: end vertex
        :param w: weight of edge (u, v)
        """
        self.E[u][v] = w

    def simpleRandomWalk(self):
        """
        The method walks through graph using simple random walk.
        Draw with 1/(n-1) probability next vertex.

        Tested for 20 independent tests
        :return: tuple:
            k - number of steps
            w - weight of path
            M - used extra storage
        """
        finalK = []
        finalW = []
        finalM = []
        finalMm = []
        finalTime = []

        for test in range(20):
            starttime = time.time()
            visited = [False for i in range(len(self.V))]
            u = 0
            visited[u] = True
            k = 0
            W = 0
            M = [0]

            while visited.count(True) != len(self.V):
                p = random.randint(0, len(self.V)-1)
                while p == u:  # go to next vertex, not stay on the same as before
                    p = random.randint(0, len(self.V)-1)
                k += 1
                W += self.E[u][p]
                u = p
                M.append(p)
                visited[u] = True
            endtime = time.time()

            finalK.append(k)
            finalW.append(W)
            finalM.append(len(M))
            finalMm.append(M)
            finalTime.append(endtime - starttime)

        for i in range(20):
            sys.stderr.write("SRW{}: {}\n".format(i, finalMm[i]))

        # wszedzie średnia
        # k - kroki, W - łączny koszt trasy, dodatkowa pamięć, M - odwiedzone wierzchołki
        return sum(finalK)/len(finalK), sum(finalW)/len(finalW), sum(finalM)/len(finalM), sum(finalTime)/len(finalTime)

    def greedyAlgorithm(self):
        """
        The method walks through graph using greedy algorithms.
        Go to the vertex with the minimal avaible weight
        :return: tuple:
            k - number of steps
            w - weight of path
            M - used extra storage
        """
        starttime = time.time()
        visited = [False for i in range(len(self.V))]
        u = 0
        visited[0] = True
        k = 0
        W = 0
        M = [0]

        while visited.count(True) != len(self.V):
            lc = [math.inf for i in range(len(self.V))]
            for i in range(len(self.E[u])):
                if i != u and not visited[i]:
                    lc[i] = self.E[u][i]

            minw = min(lc)
            idv = lc.index(minw)

            visited[idv] = True
            u = idv

            k += 1
            W += minw
            M.append(idv)

        endtime = time.time()

        sys.stderr.write("G: {}\n".format(M))
        return k, W, len(M), endtime - starttime

    def kruskalAlgorithm(self):
        """
        The method walksthrough graph using kruskal algorithm to find the minimum spanning tree.
        :return: tuple:
            k - number of steps
            w - weight of path
            M - used extra storage
        """
        self.kroki = 0
        self.S = []

        starttime = time.time()

        k = K(len(self.V))
        for i in range(len(self.E)):
            for j in range(len(self.E)):
                if i != j:
                    k.addEdge(i, j, self.E[i][j])
        T = k.kruskal()
        T2 = []  # graf eulerowski
        for t in T:
            T2.append(t)
            T2.append(t)

        # print("T", T)
        # print("T2:", T2)

        #  budowanie macierzy saśiedzctw na podstawie T2
        A = copy.deepcopy(self.E)
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] = 0

        for t in T2:
            u, v, w = t
            A[u][v] += 1
            A[v][u] += 1

        self.DFSEuler(A, 0)

        endtime = time.time()

        # obliczanie kosztu trasy
        sys.stderr.write("K {}\n".format(self.S))

        w = 0
        for s in range(len(self.S) - 2):
            w += self.E[self.S[s]][self.S[s+1]]

        return self.kroki, w, len(self.S), endtime - starttime

    def DFSEuler(self, A, v):
        """
        The method finds the euler circle
        :param A: the adjcetiv matrix
        :param v: vertex
        :return:
        """
        for i in range(len(A)):
            self.kroki += 1
            while A[v][i]:
                self.kroki += 1
                A[v][i] -= 1
                A[i][v] -= 1
                self.DFSEuler(A, i)
        self.S.append(v)

    def primAlgorithm(self):
        """
        The method walksthrough graph using prim algorithm to find the minimum spanning tree.
        :return: tuple:
            k - number of steps
            w - weight of path
            M - used extra storage
        """
        self.kroki = 0
        self.S = []

        starttime = time.time()

        p = P(len(self.V))
        for i in range(len(self.E)):
            for j in range(len(self.E)):
                if i != j:
                    p.addEdge(i, j, self.E[i][j])
        T = p.prim()
        T2 = []  # graf eulorewski
        for t in T:
            T2.append(t)
            T2.append(t)

        A = copy.deepcopy(self.E)
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] = 0

        for t in T2:
            u, v, w = t
            A[u][v] += 1
            A[v][u] += 1

        self.DFSEuler(A, 0)

        endtime = time.time()

        w = 0
        sys.stderr.write("P: {}\n".format(self.S))
        for s in range(len(self.S) - 2):
            w += self.E[self.S[s]][self.S[s+1]]

        return self.kroki, w, len(self.S), endtime - starttime


# rank = 5000
# g = Graph(rank)
# g.generate()
# #
# print(rank)
# for e in range(len(g.E)):
#     for ee in range(len(g.E)):
#         print(e, ee, g.E[e][ee])

# print("")


# ------------------------------

n = int(input())
g = Graph(int(n))
for i in range(n*n):
    q = input().split(" ")
    # print(q)

    u = int(q[0])
    v = int(q[1])
    w = int(q[2])
    g.addEdge(u, v, w)


print("SRW", g.simpleRandomWalk())
print("G", g.greedyAlgorithm())
print("K", g.kruskalAlgorithm())
print("P", g.primAlgorithm())