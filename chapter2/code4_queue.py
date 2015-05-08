__author__ = 'Administrator'


class Queue(object):
    def __init__(self):
        self.items = []
        pass

    def is_empty(self):
        return self.items == []


    def AddQ(self, item):
        self.items.insert(0, item)

    def DeleteQ(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
        pass


s = Queue()
print(s.is_empty())
s.AddQ(4)
s.AddQ("dog")
print(s.peek())
s.AddQ(True)
print(s.size())
print(s.is_empty())
s.AddQ(8.4)
print(s.items)
print(s.DeleteQ())
print(s.DeleteQ())
print(s.DeleteQ())
print(s.size())