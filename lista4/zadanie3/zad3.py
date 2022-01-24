# from zadanie1.queue import *
import math
import sys

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
        for u, v, w in result:
            sumMST += w
            print("{} {} {}".format(min(u, v), max(u, v), w))
        print("{}".format(sumMST))
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
            print("{} {} {}".format(min(u, v), max(u, v), self.E[i][parent[i]] ))

            verresult.append([min(u, v), max(u, v), self.E[i][parent[i]] ])

        print(sumMST)
        return verresult

    def minKey(self, key, mstSet):
        min = math.inf

        for v in range(len(self.V)):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index


# g = K(4)
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

# g = K(6)
# g.addEdge(0, 1, 5)
# g.addEdge(1, 2, 1)
# g.addEdge(2, 3, 2)
# g.addEdge(0, 2, 6)
# g.addEdge(1, 3, 2)
# g.addEdge(0, 3, 4)
# g.addEdge(2, 4, 5)
# g.addEdge(2, 5, 2)
# g.addEdge(4, 5, 4)
# g.addEdge(3, 5, 4)
# print(g.kruskal())

# print("\n")
# p = P(4)
# p.addEdge(0, 1, 10)
# p.addEdge(0, 2, 6)
# p.addEdge(0, 3, 5)
# p.addEdge(1, 3, 15)
# p.addEdge(2, 3, 4)

# p = P(6)
# p.addEdge(0, 1, 5)
# p.addEdge(1, 2, 1)
# p.addEdge(2, 3, 2)
# p.addEdge(0, 2, 6)
# p.addEdge(1, 3, 2)
# p.addEdge(0, 3, 4)
# p.addEdge(2, 4, 5)
# p.addEdge(2, 5, 2)
# p.addEdge(4, 5, 4)
# p.addEdge(3, 5, 4)
# print(p.prim())

def main():
    args = sys.argv
    args = args[1:][0]
    n = int(input())
    m = int(input())
    if args == "p":
        print("PRIM")
        p = P(n)
        for i in range(m):
            line = input().split()
            u, v, w = line
            p.addEdge(int(u), int(v), float(w))
        p.prim()
    elif args == "k":
        print("KRUSKAL")
        k = K(n)
        for i in range(m):
            line = input().split()
            u, v, w = line
            k.addEdge(int(u), int(v), float(w))
        k.kruskal()
    else:
        print("UNRECOGNIZED")


if __name__ == '__main__':
    main()