class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n

        l_p = 1
        for i in range(n):
            ans[i] *= l_p
            l_p *= nums[i]

        r_p = 1
        for i in range(n-1, -1, -1):
            ans[i] *= r_p
            r_p *= nums[i]
        
        return ans