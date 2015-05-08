__author__ = 'Administrator'

class Deque:
    def __init__(self):
        self.items = []
        pass

    def is_empty(self):
        return self.items is []

    def add_front(self, item):
        self.items.append(item)
        pass

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()


    def remove_rear(self):
        return self.items.pop(0)
        pass

    def size(self):
        return len(self.items)



    pass