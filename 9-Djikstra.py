import sys

def dijkstra(graph, start_vertex):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    distances[start_vertex] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        # Find the vertex with the minimum distance that hasn't been visited
        min_dist = sys.maxsize
        min_index = -1

        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                min_index = v

        if min_index == -1:
            break  # No more unvisited vertices

        u = min_index
        visited[u] = True

        # Update distances of adjacent vertices
        for v in range(num_vertices):
            if not visited[v] and graph[u][v] != 0 and distances[u] + graph[u][v] < distances[v]:
                distances[v] = distances[u] + graph[u][v]

    return distances

# Example usage:
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

start_vertex = 0
shortest_distances = dijkstra(graph, start_vertex)

print("Shortest distances from vertex", start_vertex, ":")
for i, distance in enumerate(shortest_distances):
    print(f"Vertex {i}: {distance}")