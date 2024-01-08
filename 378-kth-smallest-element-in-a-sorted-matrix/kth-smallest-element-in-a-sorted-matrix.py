class Solution:
    def countValue(self, mat, target, n):
        cnt = 0
        row, col = n-1, 0

        while row >= 0 and col < n:
            if mat[row][col] <= target:
                cnt += row + 1
                col += 1
            else:
                row -= 1
        return cnt

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[n-1][n-1]

        while l < r:
            m = l + (r-l)//2
            cnt = self.countValue(matrix, m,n)

            if cnt < k:
                l = m + 1
            else:
                r = m
        return l
        