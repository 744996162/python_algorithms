__author__ = 'Administrator'

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None, balanceFactor=0):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.blanceFactor = balanceFactor

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
        pass

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.val = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasAnyChildren():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0


    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def inorder(self, node):
        if node.leftChild:
            self.inorder(node.leftChild)
        self.print_node(node)
        if node.rightChile:
            self.inorder(node.rightChild)

        pass

    def levelorder(self, node):
        nodes = []
        nodes.append(node)
        while len(nodes)>0:
            current_node = nodes.pop(0)
            self.print_node(current_node)
            if current_node.leftChild:
                pass
        pass

    def print_node(self, node):
        pass

    def put(self, key, val):
        pass

    def _put(self, key, val, currentNode):
        pass

    def get(self, key):
        pass











    pass