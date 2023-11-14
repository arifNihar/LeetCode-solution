class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        mx = 0
        nums.sort()
        for i in range(len(nums)):
            for j  in range(i,len(nums)):
                if nums[j] - nums[i] > nums[i]:
                    break
                else:
                    if mx < nums[i]^nums[j]:
                        mx = nums[i]^nums[j]

        return mx