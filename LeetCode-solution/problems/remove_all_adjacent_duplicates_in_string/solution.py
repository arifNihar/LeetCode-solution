class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        
        for c in S:
            if len(stack) != 0 and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
                
        