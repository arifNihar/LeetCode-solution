class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sm = sum(nums)
        sm2 = 0
        for i in nums:
            for j in str(i):
                sm2 += int(j)
        return abs(sm-sm2)