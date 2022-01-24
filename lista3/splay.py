import sys
import codecs

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class splayTree:
    def __init__(self):
        self.root = None
        self.comparision = 0

    def getComparision(self):
        return self.comparision

    def __leftRotate(self, x):
        y = x.right
        x.right = y.left
        self.comparision += 1
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        self.comparision += 1
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def __rightRotate(self, x):
        y = x.left
        x.left = y.right
        self.comparision += 1
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        self.comparision += 1
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def __splay(self, x):
        self.comparision += 1
        while x.parent is not None:
            self.comparision += 1
            if x.parent.parent is None:
                self.comparision += 1
                if x == x.parent.left:
                    self.__rightRotate(x.parent)
                else:
                    self.__leftRotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zad rotation
                self.comparision += 1
                self.__rightRotate(x.parent.parent)
                self.__rightRotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag rotation
                self.comparision += 1
                self.__leftRotate(x.parent.parent)
                self.__leftRotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag rotation
                self.comparision += 1
                self.__leftRotate(x.parent)
                self.__rightRotate(x.parent)
            else:
                # zag-zig rotation
                self.comparision += 1
                self.__rightRotate(x.parent)
                self.__leftRotate(x.parent)

    def __minimium(self, node):
        """find the node with the minimium key"""
        self.comparision += 1
        while node.left is not None:
            self.comparision += 1
            node = node.left
        return node

    def __maximum(self, node):
        """find the node with the maximum key"""
        self.comparision += 1
        while node.right is not None:
            self.comparision += 1
            node = node.right
        return node

    def min(self):
        return self.__minimium(self.root).data

    def max(self):
        return self.__maximum(self.root).data

    def __join(self, s, t):
        self.comparision += 2
        if s is None:
            return t
        if t is None:
            return s

        x = self.__maximum(s)
        self.__splay(x)
        x.right = t
        t.parent = x
        return x

    def __findHelper(self, node, key):
        self.comparision += 1
        if node is None or key == node.data:
            return node
        self.comparision += 1
        if key < node.data:
            return self.__findHelper(node.left, key)
        return self.__findHelper(node.right, key)

    def find(self, k):
        x = self.__findHelper(self.root, k)
        self.comparision += 1
        if x is not None:
            # self.__splay(x)
            return 1
        return 0

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root

        self.comparision += 1
        while x is not None:
            self.comparision += 1
            y = x
            self.comparision += 1
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        self.comparision += 1
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        # splay the node
        self.__splay(node)

    def __successorHelper(self, x):
        self.comparision += 1
        if x.right is not None:
            return self.__minimium(x.right)

        y = x.parent
        self.comparision += 1
        while y is not None and x == y.right:
            self.comparision += 1
            x = y
            y = y.parent
        return y

    def successor(self, x):
        node = self.__findHelper(self.root, x)
        self.comparision += 1
        if node is not None:
            self.comparision += 1
            return self.__successorHelper(node)
        else:
            return "NO SUCCESSOR"

    def __deleteHelper(self, node, key):
        x = None
        t = None
        s = None
        self.comparision += 1
        while node is not None:
            self.comparision += 2
            if node.data == key:
                x = node
            if node.data <= key:
                node = node.right
            else:
                node = node.left

        self.comparision += 1
        if x is None:
            print("Couldnt find key in the tree")
            return

        self.__splay(x)
        self.comparision += 1
        if x.right is not None:
            t = x.right
            t.parent = None
        else:
            t = None

        s = x
        s.right = None
        x = None

        self.comparision += 1
        if s.left is not None:
            s.left.parent = None

        self.root = self.__join(s.left, t)
        s = None

    def delete(self, data):
        self.__deleteHelper(self.root, data)

    def pretty_print(self):
        self.__printHelper(self.root, "", True)

    def __printHelper(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "    "
            else:
                sys.stdout.write("L----")
                indent += "|   "

            print(currPtr.data)
            self.__printHelper(currPtr.left, indent, False)
            self.__printHelper(currPtr.right, indent, True)

    def inorder(self):
        self.__inorderHelper(self.root)

    def __inorderHelper(self, node):
        self.comparision += 1
        if node is not None:
            self.__inorderHelper(node.left)
            sys.stdout.write(str(node.data) + " ")
            self.__inorderHelper(node.right)

def prepare(s):
    """The method preapres string to insert in the tree [a-zA-Z]"""
    result = ""
    if s[0].isalpha():
        result += s[0]
    result += s[1:len(s)-1]
    if s[len(s)-1].isalpha() and len(s) > 1:
        result += s[len(s)-1]
    return result




import random
if __name__ == '__main__':
    tree = splayTree()
    # tree.insert(33)
    # tree.pretty_print()
    # print("\n")
    # tree.insert(44)
    # tree.pretty_print()
    # print("\n")
    # tree.insert(67)
    # tree.pretty_print()
    # print("\n")
    # tree.insert(5)
    # tree.pretty_print()
    # print("\n")
    # tree.insert(89)
    # tree.pretty_print()
    # print("\n")
    # tree.insert(41)
    # tree.pretty_print()
    # print("\n")
    # tree.insert(98)
    # tree.pretty_print()
    # print("\n")
    # tree.insert(1)
    # tree.pretty_print()
    # print("\n")
    # print(tree.max())
    # print(tree.min())
    # print("\n")
    # print(tree.find(1))
    # print(tree.find(2))
    # print(tree.successor(1))
    # print(tree.successor(67))
    # with codecs.open("aspell_wordlist.txt", "r", encoding="utf-8", errors="ignore") as fdata:
    #     file = fdata.read().split()
    # file = fdata.read().split()


    for q in range(100, 900, 100):
        arr = [0,0,0,0]
        toFind = []
        FF = q
        x = [i for i in range(FF)]
        # random.shuffle(x)
        index = 0
        first = 0
        mid = 0
        last = 0
        # file = open("lotr.txt", "r")
        with codecs.open("lotr.txt", "r", encoding="utf-8", errors="ignore") as fdata:
            file = fdata.read().split()
        for f in file:
            # print(f)
            if index == 0:
                first = f
            if index == (q-1):
                last = f
            if index == (q-1)//2:
                mid = f
            index += 1

            # shuffle
            # if random.uniform(0, 1) > 0.7:
            #     tree.insert(prepare(f))
            #     FF -= 1

            if FF < 0:
                break
            FF -= 1  # comment if shuffle

            if random.randint(0, 1) > 0.7:
                toFind.append(prepare(f))
        # file.close()

        print("FIRST & LAST " + str(first) + str(last))

        tree.comparision = 0
        for i in range(10):
            x = random.randint(1, len(toFind) - 1)
            # tree.comparision = 0
            tree.find(toFind[x])
            # print(tree.comparision)
        arr[3] = tree.comparision

        tree.comparision = 0
        tree.find(first)
        arr[0] = tree.comparision
        tree.comparision = 0

        tree.find(mid)
        arr[1] = tree.comparision
        tree.comparision = 0

        tree.find(last)
        arr[2] = tree.comparision
        tree.comparision = 0

        # arr[3] = tree.comparision
        # tree.comparision = 0

        # print(q, tree.comparision/10)
        print(q, arr[0], arr[1], arr[2], int(arr[3]/10))


