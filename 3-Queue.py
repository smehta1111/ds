class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.isempty():
            return self.items.pop(0)
        return None
    def peek(self):
        if not self.isempty():
            return self.items[0]
        return None
    def isempty(self):
        return len(self.items)==0
