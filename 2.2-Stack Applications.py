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
    
def infix_to_postfix(expression):
    prec = {"^":3, "*":2, "/":2, "+":1, "-":1}
    S = Stack()
    postfixList = []

    for c in expression :
        if c.isalnum():
            postfixList.append(c)
        elif c == '(':
            S.push(c)
        elif c == ')':
            topToken = S.pop()
            while topToken!= "(":
                postfixList.append(topToken)
                topToken = S.pop()
        else :
            while (not S.isempty()) and (S.peek() in prec) and (prec[S.peek()] >= prec[c]):
                postfixList.append(S.pop())
            S.push(c)
    while not S.isempty():
        postfixList.append(S.pop())
    return ''.join(postfixList)

expr = "a+b*(c^d-e)^(f+g*h)-i"
print(infix_to_postfix(expr))
