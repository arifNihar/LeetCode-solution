class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans  = []
        for i in nums:
            ans.extend([int(j) for j in list(str(i))])
        return ans
        