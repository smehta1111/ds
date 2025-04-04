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
   

def is_matched(expr):
    lefty = "({["
    righty = ")}]"
    S = Stack()
    for c in expr:
        if c in lefty:
            S.push(c)
        if c in righty:
            if S.isempty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.isempty()