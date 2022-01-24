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
