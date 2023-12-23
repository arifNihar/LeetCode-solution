class Solution:
    def cnt(self, matrix, target, n):
        count = 0
        r, c = n-1, 0

        while r >= 0 and c < n:
            if matrix[r][c] <= target:
                count += r+1
                c += 1
            else:
                r -= 1
        return count

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[n-1][n-1]

        while l < r:
            m = l + (r-l)//2
            count = self.cnt(matrix, m, n)
            
            if count < k:
                l = m + 1
            else:
                r = m
        return l
        