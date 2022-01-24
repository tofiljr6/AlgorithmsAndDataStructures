import math
from queue import PriorityQueue
import pandas as pd

class AdjList:
    aList = []

    def __init__(self, size):
        self.aList = [[x] for x in range(size)]

    def add_edge(self, u, v, weight):
        self.aList[u].append({'v': v, 'w': weight})
        self.aList[v].append({'v': u, 'w': weight})


def isExist(Q, node):
    for i in Q.queue:
        if i[2] == node:
            return True
    return False

def getAdjV(V):
    adjVs = []
    for i in range(1, len(V)):
        adjVs.append(V[i]['v'])
    return adjVs

def getqKey(Q, v):
    q = Q.queue
    for j in q:
        if j[2] == v:
            return j[0]

def w(a, u, v):
    u = a[u]  # Get u's adjacency list
    for i in range(1, len(u)):
        if u[i]['v'] == v:
            return u[i]['w']
    return math.inf

def keepHeap(Q):
    R = PriorityQueue()
    while not Q.empty():
        R.put(Q.get())
    return R

def MST_Prim(a, r):
    # Store all points in the graph
    V = []
    for i in range(1, 8):
        V.append({'key': math.inf, 'Π': None, 'node': i})
    V[r]['key'] = 0

    # Create priority queue
    Q = PriorityQueue()
    for i in range(7):
        # All clicks into the queue
        Q.put([V[i]['key'], V[i]['Π'], V[i]['node']])
    print(Q.queue)

    wsum = []
    mst = []
    while not Q.empty():

        minV = Q.get()  # Out of the queue with the smallest key value

        wsum.append(minV[0])
        mst.append(minV[2])
        u = minV[2]  # Get which node
        for v in getAdjV(a[u]):
            if isExist(Q, v) and w(a, u, v) < getqKey(Q, v):
                for j in Q.queue:
                    if j[2] == v:
                        j[1] = u
                        j[0] = w(a, u, v)
                        break
            Q = keepHeap(Q)  # After modifying the value of the node in the priority queue, it is necessary to maintain the nature of the small top heap
        print(Q.queue)  # Print priority queue

    # Print the sum of the weights of MST
    print("MST weight sum: %d" % sum(wsum))

    # Print the edge with the largest weight on the MST
    print("Maximum weight on MST: %d" % max(wsum))

    # Print the nodes on MST in turn
    print("The nodes of MST are:", mst)

if __name__ == '__main__':
    # Read data
    input_nums = pd.read_table('input_exp7.txt', header=None, sep=" ")
    v_number = input_nums.iloc[0, 0]
    e_number = input_nums.iloc[0, 1]
    adjList = AdjList(v_number + 1)
    for i in range(1, input_nums.shape[0]):
        adjList.add_edge(input_nums.iloc[i, 0], input_nums.iloc[i, 1], input_nums.iloc[i, 2])

    # Get adjacency list
    a = adjList.aList
    for i in a:
        print(i)

    # The parameters are the adjacency table and MST starting point
    MST_Prim(a, 1 - 1)

