class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.isempty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.isempty():
            return self.items[-1]
        return None
    def isempty(self):
        return len(self.items)==0
