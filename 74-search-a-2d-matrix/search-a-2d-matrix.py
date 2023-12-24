class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, r = 0, r*c - 1

        while l <= r:
            m = (l+r)//2
            m_e = matrix[m//c][m%c]

            if m_e == target:
                return 1
            elif m_e < target:
                l = m+1
            else:
                r = m - 1
        return 0