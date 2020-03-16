from queue import *
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inBounds(i,j):
            return not(i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1)
        
        myQ = Queue()
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == 2:
                    myQ.put((r,c,0))
        
        visited = [[False]*len(grid[0]) for _ in range(0,len(grid))]
        depth = 0
        while not myQ.empty():
            i,j,depth = myQ.get()
            visited[i][j] = True
            grid[i][j] = 2
            directions = [[0,-1], [0,1], [1,0], [-1,0]]
            for direction in directions:
                if inBounds(i+direction[0], j+direction[1]) and not visited[i+direction[0]][j+direction[1]] and grid[i+direction[0]][j+direction[1]] == 1:
                    myQ.put((i+direction[0], j+direction[1], depth+1))
                    
        
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1:
                    return -1
    
        return depth