class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        if not A:
            return 0
        
        n = len(A)
        l = [1]*n

        for i in range(1, n):
            for j in range(i):
                if A[i] > A[j]:
                    l[i] = max(l[i], l[j]+1)
        return max(l)