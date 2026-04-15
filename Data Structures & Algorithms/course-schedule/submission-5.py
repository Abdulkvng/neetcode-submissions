class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
# keeps track of perequisites 
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            #for pair in prerequisites:
    #crs = pair[0]
    #pre = pair[1]

            preMap[crs].append(pre)
        VS = set()
        def dfs(crs):
                #base
            if crs in VS:
                return False
            if preMap[crs] == []:
                return True

            VS.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            VS.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

            
        




        