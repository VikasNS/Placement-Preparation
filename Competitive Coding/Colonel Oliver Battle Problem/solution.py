T = int(input().strip())

class Node():
    def __init__(self):
        self.adjacentNodes = []
        
    def addAdjacentNode(self , node):
        self.adjacentNodes.append(node)

def Count(ele,seen):
    stack = [ele]
    i = 0
    while(len(stack)>0):
        ele = stack.pop()
        i+=1
        seen.add(ele)
        for adjNodes in ele.adjacentNodes:
            if adjNodes not in seen:
                stack.append(adjNodes)
    return [i,seen]
    
    
for _ in range(T):
    rows , columns = [int(ele) for ele in input().strip().split()]
    matrix = []
    
    for __ in range(rows):
        matrix.append([-1 if(ele == "0") else Node() for ele in input().strip().split()])
    
    for row in range(rows):
        for column in range(columns):
            if(matrix[row][column] != -1):
                currNode = matrix[row][column]
                
                if(row-1<rows and row-1>=0 and column+1<columns and column+1>=0):
                    if(matrix[row-1][column+1] != -1):
                        currNode.addAdjacentNode(matrix[row-1][column+1])
                        
                if(row-1<rows and row-1>=0 and column<columns and column>=0):
                    if(matrix[row-1][column] != -1):
                        currNode.addAdjacentNode(matrix[row-1][column])
                        
                if(row-1<rows and row-1>=0 and column-1<columns and column-1>=0):
                    if(matrix[row-1][column-1] != -1):
                        currNode.addAdjacentNode(matrix[row-1][column-1])
                        
                if(row<rows and row>=0 and column-1<columns and column-1>=0):
                    if( matrix[row][column-1] != -1):
                        currNode.addAdjacentNode(matrix[row][column-1])
                        
                if(row+1<rows and row+1>=0 and column-1<columns and column-1>=0):
                    if(matrix[row+1][column-1] != -1):
                        currNode.addAdjacentNode(matrix[row+1][column-1])
                        
                if(row+1<rows and row+1>=0 and column<columns and column>=0):
                    if( matrix[row+1][column] != -1):
                        currNode.addAdjacentNode(matrix[row+1][column])
                        
                if(row+1<rows and row+1>=0 and column+1<columns and column+1>=0):
                    if(matrix[row+1][column+1] != -1):
                        currNode.addAdjacentNode(matrix[row+1][column+1])
                        
                if(row<rows and row>=0 and column+1<columns and column+1>=0):
                    if( matrix[row][column+1] != -1):
                        currNode.addAdjacentNode(matrix[row][column+1])
    
    seen = set()
    i = 0
    j = 0
    count = 0
    for eachRow in matrix:
        for eachEle in eachRow:
            if eachEle != -1:
                if eachEle not in seen:
                    i+=1
                    tempCount,seen = Count(eachEle,seen)
                    if(tempCount > count):
                        count = tempCount
                        j = i
    print(j,count)
    
    
    
    
    
        
