class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        p = 0
        if n*m == len(original):
            for i in range(m):
                x = []
                for j in range(n):
                    x.append(original[p])
                    p += 1
                ans.append(x)
        return ans