__author__ = 'Administrator'

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None
        pass

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = new_node
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
        pass

    def insert_right(self, item):
        pass

    def get_left_child(self):
        pass

    def get_right_child(self):
        pass

    def set_root_val(self, obj):
        pass

    def get_root_val(self):
        pass
