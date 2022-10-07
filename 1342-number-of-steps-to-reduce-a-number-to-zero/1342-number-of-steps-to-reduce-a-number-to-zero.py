class Solution:
    def numberOfSteps(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n%2 == 0:
                n //= 2
                ans += 1
            else:
                n -= 1
                ans += 1
        return ans