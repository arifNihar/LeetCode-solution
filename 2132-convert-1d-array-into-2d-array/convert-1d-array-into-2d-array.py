class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if n*m == len(original):
            for i in range(m):
                ans.append(original[i * n : (i + 1) * n])
        return ans