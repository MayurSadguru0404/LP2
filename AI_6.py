# single source shortest path
import sys
graph={}
n=int(input("Enter number of edges:"))
for i in range(n):
    s,d,w=input("Enter source destination weight: ").split()
    w=int(w)
    
    if s not in graph:
        graph[s]={}
    graph[s][d]=w
source=input("Enter source node:")
dist={node: sys.maxsize for node in graph}
dist[source]=0
unvisited=set(graph.keys())

while unvisited:
    current=min(unvisited,key=lambda node: dist[node])
    unvisited.remove(current)
    for neighbor,weight in graph[current].items():
        new_dist=dist[current]+weight
        if new_dist < dist.get(neighbor,sys.maxsize):
            dist[neighbor] = new_dist

print("Shortest Distances:")
for node in dist:
    print(node,"=",dist[node])
    
"""Enter number of edges: 5

A B 2
A C 4
B C 1
B D 7
C D 3

Enter source node: A
"""

#job scheduling
jobs=[]
n=int(input("Enter number of jobs:"))
for i in range(n):
    name=input("Enter Job name:")
    profit=int(input("Enter profit:"))
    deadline=int(input("Enter deadline:"))
    jobs.append((name,profit,deadline))

jobs.sort(key=lambda x: x[1],reverse=True)
slots=[False]*n
result=["-"]*n
total_profit=0

for job in jobs:
    name,profit,deadline=job
    for j in range(min(n,deadline)-1,-1,-1):
        if not slots[j]:
            slots[j]=True
            result[j]=name
            total_profit+= profit
            break
print("Scheduled Jobs:",result)
print("Total Profit:",total_profit)
        
"""Enter number of jobs: 4

Enter job name: J1
Enter profit: 100
Enter deadline: 2

Enter job name: J2
Enter profit: 50
Enter deadline: 1

Enter job name: J3
Enter profit: 150
Enter deadline: 2

Enter job name: J4
Enter profit: 200
Enter deadline: 1
"""