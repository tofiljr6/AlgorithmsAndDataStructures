import sys


class Node():
    def __init__(self, data):
        self.data = data  # holds the key
        self.parent = None  # pointer to the parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child
        self.color = 1  # 1 . Red, 0 . Black


class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.comparision = 0

    def getComparision(self):
        return self.comparision

    def __leftRotate(self, x):
        """The method rotates left at node x"""
        y = x.right  # set y
        x.right = y.left
        self.comparision += 1
        if x.left != self.TNULL:
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
        """The method rotates right at node x"""
        y = x.left  # set y
        x.left = y.right
        self.comparision += 1
        if y.right != self.TNULL:
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

    def insert(self, key):
        """The method insert new node with value key in the tree"""
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # new node must be red

        y = None
        x = self.root

        self.comparision += 1
        while x != self.TNULL:
            self.comparision += 1
            y = x
            self.comparision += 1
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y

        self.comparision += 1
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self.comparision += 1
        if node.parent is None:
            node.color = 0
            return

        self.comparision += 1
        if node.parent.parent is None:
            return

        self.__insertFixup(node)

    def __insertFixup(self, k):
        """The method fixs rbt tree after insert new value"""
        self.comparision += 1
        while k.parent.color == 1:
            self.comparision += 1
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                self.comparision += 1
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    self.comparision += 1
                    if k == k.parent.left:
                        k = k.parent
                        self.__rightRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.__leftRotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle
                self.comparision += 1
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    self.comparision += 1
                    if k == k.parent.right:
                        k = k.parent
                        self.__leftRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.__rightRotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __transplant(self, u, v):
        """The method transplant the tree"""
        self.comparision += 1
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __minimum(self, node):
        """The method finds the node with the minimum key"""
        self.comparision += 1
        while node.left != self.TNULL:
            self.comparision += 1
            node = node.left
        return node

    def __maximum(self, node):
        """The method finds the node with the maximum key"""
        self.comparision += 1
        while node.right != self.TNULL:
            self.comparision += 1
            node = node.right
        return node

    def max(self):
        return self.__maximum(self.root).data

    def min(self):
        return self.__minimum(self.root).data

    def __deleteHelper(self, node, key):
        """The method deletes the node with key data in the tree"""
        z = self.TNULL
        self.comparision += 1
        while node != self.TNULL:
            self.comparision += 1
            if node.data == key:
                z = node

            self.comparision += 1
            if node.data <= key:
                node = node.right
            else:
                node = node.left

        self.comparision += 1
        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return

        y = z
        yOriginalColor = y.color
        self.comparision += 1
        if z.left == self.TNULL:
            x = z.right
            self.__transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = self.__minimum(z.right)
            yOriginalColor = y.color
            x = y.right
            self.comparision += 1
            if y.parent == z:
                x.parent = y
            else:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        self.comparision += 1
        if yOriginalColor == 0:
            self.__fixDelete(x)

    def delete(self, data):
        """The method deletes the node with key data in the tree starts form root"""
        self.__deleteHelper(self.root, data)

    def __fixDelete(self, x):
        """The method fixs the rb tree modified by the delete operation"""
        self.comparision += 1
        while x != self.root and x.color == 0:
            self.comparision += 1
            if x == x.parent.left:
                s = x.parent.right
                self.comparision += 1
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.__leftRotate(x.parent)
                    s = x.parent.right
                self.comparision += 1
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    self.comparision += 1
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.__rightRotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.__leftRotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                self.comparision += 1
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.__rightRotate(x.parent)
                    s = x.parent.left
                self.comparision += 1
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    self.comparision += 1
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.__leftRotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.__rightRotate(x.parent)
                    x = self.root
        x.color = 0

    def __findHelper(self, node, key):
        """The method helps find a node with value key"""
        self.comparision += 1
        if node == self.TNULL or key == node.data:
            return node
        self.comparision += 1
        if key < node.data:
            return self.__findHelper(node.left, key)
        return self.__findHelper(node.right, key)

    def find(self, k):
        """The method finds k value in the tree and returns 0 if is not, 1 otherwise"""
        if self.__findHelper(self.root, k) != self.TNULL:
            return 1
        return 0

    def successor(self, data):
        """The method returns succesor from value"""
        node = self.__findHelper(self.root, data)
        if node != self.TNULL:
            return self.__successorHelper(self.__findHelper(self.root, data)).data
        else:
            return "NO SUCCESSOR"

    def __successorHelper(self, x):
        """The method return succesor from node"""
        self.comparision += 1
        if x.right != self.TNULL:
            return self.__minimum(x.right)
        y = x.parent
        self.comparision += 1
        while y != self.TNULL and x == y.right:
            self.comparision += 1
            x = y
            y = y.parent
        return y

    def prettyPrinter(self):
        self.__printHelper(self.root, "", True)

    def __printHelper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "    "
            else:
                sys.stdout.write("L----")
                indent += "|   "
            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.__printHelper(node.left, indent, False)
            self.__printHelper(node.right, indent, True)

    def inorder(self):
        self.__inorderHelper(self.root)

    def __inorderHelper(self, node):

        self.comparision += 1
        if node != self.TNULL:
            self.__inorderHelper(node.left)
            print(str(node.data), end=" ")
            self.__inorderHelper(node.right)


# rbt = RedBlackTree()
# rbt.insert("aa")
# rbt.insert("b")
# rbt.insert("c")
# rbt.insert("d")
# # rbt.insert("af")
# # rbt.insert("ef")
# # rbt.insert("afs")
# # rbt.insert("asfa")
# # rbt.inorder()
# print("\n")
# rbt.prettyPrinter()
# # rbt.delete("ef")
# # rbt.prettyPrinter()
# print(rbt.find("e"))
# print(rbt.find("efe11"))
# print(rbt.successor("ac"))
# print(rbt.max())
# print(rbt.min())

# def doWork():
#     args = sys.argv
#     args = args[1:]
#
#     rbt = RedBlackTree()
#     operation = {
#         "insert": 0,
#         "inorder": 0,
#         "delete": 0,
#         "max": 0,
#         "min": 0,
#         "find": 0,
#         "load": 0,
#         "successor": 0
#     }
#     elems, delems = 0, 0
#     if len(args) == 0:
#         print("No argument")
#     else:
#         pass
#
# import bst as bst
# root = None
# root = bst.insert(root, 30)
# bst.inOrder(root)
