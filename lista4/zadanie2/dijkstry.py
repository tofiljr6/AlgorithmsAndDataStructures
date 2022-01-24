import math
import sys
import time

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
            if self.A[i].value == x and self.A[i].p < bigger_p:
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


class Graph:
    def __init__(self):
        self.V = []
        self.E = [[]]

    def dijstra(self, src):
        # prepare
        dist = [math.inf for _ in range(len(self.V))]
        prev = [None for _ in range(len(self.V))]
        dist[src] = 0

        # make a priority queue
        H = Queue()
        for i in range(len(self.V)):
            H.insert(self.V[i], dist[i])

        while not H.empty():
            u = H.pop()
            for z in range(len(self.E[u.value])):
                # print(u, self.E[u.value][z], end=" ")
                if self.E[u.value][z] != 0:
                    if dist[z] > round(dist[u.value] + self.E[u.value][z], 6):
                        dist[z] = round(dist[u.value] + self.E[u.value][z], 6)
                        prev[z] = u.value
                        H.decreasekey(z, dist[z])
        return dist, prev

    def goDijstra(self, src):
        dist, prev = self.dijstra(src)
        print(dist)
        print(prev)
        paths = []

        for p in range(0, len(prev)):
            path = []
            x = prev[p]
            if x is not None:
                path.append(p)
                path.append(x)
                while x != src:
                    x = prev[x]
                    path.append(x)

            else:
                path = []
            paths.append(path)

        for i in range(len(paths)):
            print(i, dist[i])
            sys.stderr.write("{} {}\n".format(i, paths[i][::-1]))   # uncomment

    def print(self):
        for i in self.E:
            print(i)


def main():

    g = Graph()
    vgraph = int(input())
    egraph = int(input())
    # print(vgraph, egraph)

    g.V = [i for i in range(vgraph)]
    g.E = [[0.0 for i in range(len(g.V))] for j in range(len(g.V))]
    for edge in range(egraph):
        f = input()
        f = f.split(" ")
        while "" in f:
            f.remove("")
        s = int(f[0])
        e = int(f[1])
        w = float(f[2].rsplit("\n")[0])
        g.E[s][e] = w
    src = int(sys.argv[1:][0])
    starttime = time.time()
    g.goDijstra(src)
    endtime = time.time()
    deltatime = round(endtime - starttime, 10)
    sys.stderr.write("time: {}\n".format(deltatime))

    # TESTS = 5
    # finaltime = 0
    # for test in range(TESTS):
    #     starttime = time.time()
    #     g.goDijstra(src)
    #     endtime = time.time()
    #     deltatime = round(endtime - starttime, 10)
    #     finaltime += deltatime
    # sys.stderr.write("{}\n".format(finaltime/TESTS))


if __name__ == "__main__":
    # python3 dijkstry.py 5 < ./inputdata/g8.txt 2> out.txt
    #                     ^----- wierzchołek startowy
    main()
