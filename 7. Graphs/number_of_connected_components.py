from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(nodeNum, visited):
            if nodeNum in visited:
                return
            visited.add(nodeNum)
            neighbors = adjList[nodeNum]
            for neighbor in neighbors:
                dfs(neighbor, visited)
                
        adjList = defaultdict(list)
        
        for item in edges:
            adjList[item[0]].append(item[1])
            adjList[item[1]].append(item[0])
        
        visited = set()                       
        connectedComponent = 0
        for nodeNum in range(0, n):
            if nodeNum not in visited:
                connectedComponent += 1
                dfs(nodeNum, visited)
                
        return connectedComponent