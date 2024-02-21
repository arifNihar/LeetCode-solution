class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest_streak = 0
        if len(nums) != 0:
            longest_streak = 1
        else:
            return 0  # Initialize the longest streak
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)