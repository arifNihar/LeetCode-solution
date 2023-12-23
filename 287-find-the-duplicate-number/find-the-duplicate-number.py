class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = {}
        for i in nums:
            if i in ans:
                return i
            else:
                ans[i] = 1
        return None