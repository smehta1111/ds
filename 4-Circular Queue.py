class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]* size
        self.front = -1
        self.rear = -1

    def isempty(self) :
        return self.front == -1 
    
    def isfull(self):
        return (self.rear+1)%self.size == self.front

    def enqueue(self,item):
        if self.isfull():
            print("Queue is full")
        else : 
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = item
    
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else : 
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front+1)%self.size
            return item
    
    def peek(self):
        if self.isempty():
            print("Queue is empty")
        else : 
            return self.queue[self.front]
    
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else : 
            elements = []
            i = self.front 
            while i != self.rear:
                elements.append(self.queue[i])
                i = (i+1)%self.size
            elements.append(self.queue[self.rear])
            print(f"Queue : {elements}")
    