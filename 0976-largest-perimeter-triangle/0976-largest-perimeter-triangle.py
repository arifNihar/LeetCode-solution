class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        ans = 0
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1]+nums[i+2]:
                ans = max(ans,nums[i]+nums[i+1]+nums[i+2])
                break
        return ans