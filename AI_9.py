n=int(input("Enter number of queens:"))
board=[[0 for i in range(n)]for j in range(n)]

def is_safe(row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    i=row
    j=col  
    while i>= 0 and j >=0:
        if board[i][j]==1:
            return False
        i -=1
        j -=1
    
    i = row
    j=col
    while i <n and j >=0:
        if board[i][j]==1:
            return False
        i+=1
        j-=1
    return True

def solve(col):
    if col>=n:
        return True
    for i in range(n):
        if is_safe(i,col):
            board[i][col]=1
            if solve(col+1):
                return True
            board[i][col]=0
    return False

if solve(0):
    print("Solution Found:\n")
    for row in board:
        print(row)
else:
    print("No Solution")

        