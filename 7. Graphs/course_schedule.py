class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
            
        def isCycle(currentNode, currentPath, visited, adjList):
            if currentNode in currentPath:
                return True
            currentPath.add(currentNode)
            visited.append(currentNode)
            for neighbor in adjList[currentNode]:
                if neighbor in currentPath:
                    return True
                if neighbor not in visited:
                    if isCycle(neighbor, currentPath, visited, adjList):
                        return True
            currentPath.remove(currentNode)
            return False
            
            
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visited = []
        for key in adjList.keys():
            if key not in visited:
                if (isCycle(key, set(), visited, adjList)):
                    return False
            
            
        return len(visited) == numCourses