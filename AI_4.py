from queue import PriorityQueue

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Heuristic Function
def heuristic(state):
    count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count

# Find blank space
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def convert(state):
    return tuple(tuple(row) for row in state)

def moves(state):
    x, y = find_blank(state)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    children = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            children.append(new_state)

    return children

# Check solvability
def is_solvable(state):
    arr = []
    for row in state:
        for num in row:
            if num != 0:
                arr.append(num)
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1

    return inversions % 2 == 0

# Print puzzle
def print_state(state):
    for row in state:
        print(row)
    print()

# Input initial state
print("Enter initial state row-wise:")

start = []

for i in range(3):
    row = list(map(int, input().split()))
    start.append(row)
    
if is_solvable(start):
    print("Puzzle is Solvable")
else:
    print("Puzzle is Not Solvable")

# A* Search
pq = PriorityQueue()

pq.put((heuristic(start), start))

visited = set()

while not pq.empty():

    h, current = pq.get()

    print_state(current)

    if current == goal:
        print("Goal State Reached")
        break

    visited.add(convert(current))

    for child in moves(current):

        if convert(child) not in visited:
            pq.put((heuristic(child), child))