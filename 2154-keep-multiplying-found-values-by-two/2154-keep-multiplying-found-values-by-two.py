class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while 1:
            if original in nums:
                original *= 2
            else:
                break
        return original