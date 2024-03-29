# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, l, ans):
            if not node:
                return
            if l == len(ans):
                ans.append(node.val)
            dfs(node.right, l+1, ans)
            dfs(node.left, l+1, ans)
        dfs(root, 0, ans)
        return ans