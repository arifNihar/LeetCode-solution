class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        fre = {}
        for i in nums:
            if i not in fre:
                fre[i] = 1
            else:
                fre[i] += 1
        
        for i in range(1,len(nums)+1):
            if i not in fre:
                ans.append(i)
        return ans