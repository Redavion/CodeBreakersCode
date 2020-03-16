class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
   
        def dfs(currentNode, currentPath):
            if currentNode in coursesTaken:
                return True
            if currentNode in currentPath:
                return False
            currentPath.add(currentNode)

            if currentNode in adjList:
                for neighbor in adjList[currentNode]:
                    if not dfs(neighbor, currentPath):
                        return False
            ans.append(currentNode)
            coursesTaken.add(currentNode)
            currentPath.remove(currentNode)
            return True
            
        #make an adjacentlist
        adjList = {}
        for source, dest in prerequisites:
            if source in adjList:
                adjList[source].append(dest)
            else:
                adjList[source] = [dest]
                
        ans= []
        coursesTaken = set()
        for course in range(numCourses):
            if not dfs(course, set()):
                return []
        
        return ans
    