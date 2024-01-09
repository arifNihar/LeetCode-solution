class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        mx = max(arr)
        ans = arr.index(mx)
        return ans