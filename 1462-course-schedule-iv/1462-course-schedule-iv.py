class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #Make the matrix with all false
        matrix = [[False] * numCourses for _ in range(numCourses)]

        #take the pre-req and mark all False -> True
        for pre, crs in prerequisites:
            matrix[pre][crs] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if matrix[i][k] and matrix[k][j]:
                        matrix[i][j] = True
        
        res = []
        for u,v in queries:
            res.append(matrix[u][v])
        return res


        