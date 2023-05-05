import pdb

class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
    
    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return None

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        count = 0
        # pdb.set_trace()
        for item in self.items:
            if target == item:
                return len(self.items) - count -1
            else:
                count += 1
                
        return -1
