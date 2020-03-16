class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        

        def isEventuallySafe(currentNode, currentPath, graph, eventuallySafe):
            if eventuallySafe[currentNode]:
                return True
            if len(graph[currentNode]) == 0:
                eventuallySafe[currentNode] = True;
                return eventuallySafe[currentNode]
            if currentNode in currentPath:
                return False
            
            currentPath.add(currentNode)
            for node in graph[currentNode]:
                if not isEventuallySafe(node, currentPath, graph, eventuallySafe):
                    return False
            currentPath.remove(currentNode)
            eventuallySafe[currentNode] = True
            return True
        
        eventuallySafe = [False] * len(graph)
        ansList = []
        for currentNode, outgoingEdges in enumerate(graph):
            if eventuallySafe[currentNode]:
                ansList.append(currentNode)
            else:
                if (isEventuallySafe(currentNode, set(), graph, eventuallySafe)):
                    ansList.append(currentNode)
        return ansList
    