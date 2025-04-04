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
    
def dfs(graph,start):
    visited = {node: False for node in graph}
    S = Stack()
    S.push(start)
    while not S.isempty():
        vertex = S.pop()
        if not visited[vertex]:
            print(vertex, end=" ")
            visited[vertex] = True
            for neighbour in reversed(graph[vertex]):
                if not visited[neighbour]:
                    S.push(neighbour)


g = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'D']
}

print("DFS starting from A:")
dfs(g,'A')