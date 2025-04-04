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
    

def evaluate_postfix(expression):
    s = Stack()
    
    for token in expression.split():
        if token.isalnum():  
            s.append(token)
        else: 
            b = s.pop()
            a = s.pop()
            if token == '+':
                s.append(a + b)
            elif token == '-':
                s.append(a - b)
            elif token == '*':
                s.append(a * b)
            elif token == '/':
                s.append(a / b) 
            elif token == '**':
                s.append(a ** b)
    
    return s.pop()  


expression = "3 4 + 2 * 7 /" 
result = evaluate_postfix(expression)
print("Result:", result)
