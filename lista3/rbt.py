class Node:
    """Interpretation of single node in the binary tree"""

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = None


def leftRotate(root, x):
    y = x.right
    x.right = y.left
    if y.left != root:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == root:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y


def rightRotate(root, x):
    y = x.right
    x.right = y.left
    if y.right != root:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == root:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.right = x
    x.parent = y


def rbInsertFixUp(root, z):
    while z.parent.color == "RED":
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == "RED":
                z.parent.color = "BLACK"
                y.color = "BLACK"
                z.parent.parent.color = "RED"
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    leftRotate(root, z)
                z.parent.color = "BLACK"
                z.parent.parent.color = "RED"
                rightRotate(root, z.parent.parent)
        else:
            z.parent.left, z.parent.right = z.parent.right, z.parent.left
    root.color = "BLACK"


def rbInsert(root, z):
    y = root
    x = root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == root:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = None
    z.right = None
    z.color = "RED"
    rbInsertFixUp(root, z)


root = None
rbInsert(root, Node(40))
