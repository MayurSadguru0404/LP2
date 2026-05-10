# Kruskal's Minimum Spanning Tree Algorithm
edges = []
n = int(input("Enter number of edges: "))

for i in range(n):
    u, v, w = input("Enter source destination weight: ").split()
    edges.append((int(w), u, v))
edges.sort()
parent = {}

# Find function
def find(node):
    if parent[node] == node:
        return node
    return find(parent[node])

# Union function
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    parent[root2] = root1

# Initialize parent
for edge in edges:
    w, u, v = edge
    parent[u] = u
    parent[v] = v

print("Edges in MST:")

for edge in edges:
    w, u, v = edge
    if find(u) != find(v):
        union(u, v)
        print(u, "-", v, ":", w)
        
"""Enter number of edges: 5

A B 1
A C 5
B C 3
B D 4
C D 2"""

#DIJKSTRAS
import sys
graph = {}
n = int(input("Enter number of edges: "))

for i in range(n):
    s, d, w = input("Enter source destination weight: ").split()
    w = int(w)
    if s not in graph:
        graph[s] = {}
    graph[s][d] = w

source = input("Enter source node: ")
dist = {node: sys.maxsize for node in graph}
dist[source] = 0
unvisited = set(graph.keys())

while unvisited:
    current = min(unvisited, key=lambda node: dist[node])
    unvisited.remove(current)
    for neighbor, weight in graph[current].items():
        new_dist = dist[current] + weight
        if new_dist < dist.get(neighbor, sys.maxsize):
            dist[neighbor] = new_dist

print("Shortest Distances:")
for node in dist:
    print(node, "=", dist[node])
    
"""Enter number of edges: 5

A B 2
A C 4
B C 1
B D 7
C D 3

Enter source node: A"""