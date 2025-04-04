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


def bfs(graph, start):
    visited = {node: False for node in graph}
    Q = Queue()
    Q.enqueue(start)
    while not Q.isempty():
        vertex = Q.dequeue()
        if not visited[vertex]:
            print(vertex, end=" ")
            visited[vertex] = True
            for neighbour in graph[vertex]:
                if not visited[neighbour]:
                    Q.enqueue(neighbour)

g = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'D']
}

print("BFS starting from A:")
bfs(g, 'A')