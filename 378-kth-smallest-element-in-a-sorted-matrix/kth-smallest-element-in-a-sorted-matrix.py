class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pos = []
        for i in range(len(matrix)):
            pos.extend(matrix[i])
        pos.sort()
        return pos[k-1]

        
        