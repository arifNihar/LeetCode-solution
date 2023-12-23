class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        fre = [0]*(len(nums)+1)
        
        for i in nums:
            if fre[i] == 0:
                fre[i] = 1
        
        for i in range(1,len(nums)+1):
            if fre[i] == 0:
                ans.append(i)
        return ans