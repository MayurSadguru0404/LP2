graph = {}
n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex name: ")
    neighbors = input(f"Enter neighbors of {vertex} separated by space: ").split()
    graph[vertex] = neighbors
visited = set()

def dfs(vertex):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(neighbor)

start = input("Enter starting vertex: ")
print("DFS Traversal:")
dfs(start)

"""Enter number of vertices: 5

Enter vertex name: A
Enter neighbors of A separated by space: B C

Enter vertex name: B
Enter neighbors of B separated by space: A D E

Enter vertex name: C
Enter neighbors of C separated by space: A

Enter vertex name: D
Enter neighbors of D separated by space: B

Enter vertex name: E
Enter neighbors of E separated by space: B

Enter starting vertex: A"""