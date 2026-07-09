class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adj = [[] for _ in range (numCourses)]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1

        queue = deque()
        for i in range (numCourses):
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            j = queue.popleft()
            numCourses -= 1
            for k in adj[j]:
                indeg[k] -= 1
                if indeg[k] == 0:
                    queue.append(k)
        
        if numCourses == 0:
            return True
        else: 
            return False
        
        