N=4
def print_board(board):
    for row in board:
        print(row)
        
def heuristic(board):
    attacks=0
    
    for i in range(N):
        for j in range(i+1,N):
            if board[i]==board[j]:
                attacks+=1
            if abs(board[i]-board[j])==abs(i-j):
                attacks+=1
    return attacks

def solve():
    board=[0]*N
    col=0
    
    while col<N:
        min_h=999
        best_row=0
        
        for row in range(N):
            board[col]=row
            h=heuristic(board)
            
            if h < min_h:
                min_h=h
                best_row=row
        board[col]=best_row
        col+=1
    return board

solution=solve()
print("Queen Positions:")
print(solution)

print("\nChess Board:")
for i in range(N):
    for j in range(N):
        if solution[j]==i:
            print("Q",end=" ")
        else:
            print(".",end=" ")
    print()
