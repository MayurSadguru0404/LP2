# Prim's Minimum Spanning Tree Algorithm
INF = 999999
n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
selected = [False] * n
selected[0] = True

print("Edge : Weight")

for i in range(n - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j]:
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", graph[x][y])
    selected[y] = True
    
# """Enter number of vertices: 4

# Enter adjacency matrix:
# 0 10 6 5
# 10 0 0 15
# 6 0 0 4
# 5 15 4 0"""

#Kruskals
edges=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    u,v,w=input("Enter source destination weight:").split()
    edges.append((int(w),u,v))
edges.sort()
parent={}

def find(node):
    if parent[node]==node:
        return node
    return find(parent[node])

def union(u,v):
    root1=find(u)
    root2=find(v)
    parent[root2]=root1
    
for edge in edges:
    w,u,v=edge
    parent[u]=u
    parent[v]=v
print("Edges in MST:")

for edge in edges:
    w,u,v=edge
    if find(u) != find(v):
        union(u,v)
        print(u,"-",v,":",w)
        
"""Enter number of edges: 5

A B 1
A C 5
B C 3
B D 4
C D 2"""