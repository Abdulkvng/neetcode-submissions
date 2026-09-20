class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        prereq = [set() for _ in range(numCourses)]

        def dfs(start, course):
            for nxt in graph[course]:
                if nxt not in prereq[start]:
                    prereq[start].add(nxt)
                    dfs(start, nxt)

        for i in range(numCourses):
            dfs(i, i)

        return [v in prereq[u] for u, v in queries]



