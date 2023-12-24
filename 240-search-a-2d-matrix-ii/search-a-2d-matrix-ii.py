class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        s, e = 0, c-1

        while s < r and e >= 0:
            m_e = matrix[s][e]

            if m_e == target:
                return 1
            elif m_e < target:
                s += 1
            else:
                e -= 1
        return 0