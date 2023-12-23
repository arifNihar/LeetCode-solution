class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        r,c = len(matrix), len(matrix[0])
        pos = []
        for i in range(r):
            pos.extend(matrix[i])
        pos.sort()
        return pos[k-1]

        
        