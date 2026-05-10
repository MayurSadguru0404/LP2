graph={}
n=int(input("Enter number of vertices:"))
for i in range(n):
    vertex=input("Enter vertex names:")
    neighbors=input(f"Enter neighbors of {vertex} seperated by spaces:").split()
    graph[vertex]=neighbors
start=input("Enter staring vertex:")

visited=[]
queue=[]

def bfs(start):
    visited.append(start)
    queue.append(start)
    
    while queue:
        vertex=queue.pop(0)
        print(vertex,end=" ")
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
print("BFS Traversal:")
bfs(start)

"""Enter number of vertices: 5

Enter vertex name: A
Enter neighbors of A: B C

Enter vertex name: B
Enter neighbors of B: A D E

Enter vertex name: C
Enter neighbors of C: A

Enter vertex name: D
Enter neighbors of D: B

Enter vertex name: E
Enter neighbors of E: B

Enter starting vertex: A
A B C D E
"""