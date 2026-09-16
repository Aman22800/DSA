# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node,currSum):
            if not node:
                return 0
            currSum=str(currSum)+str(node.val)
            if not node.left and not node.right:
                return int(currSum)
            return dfs(node.left,currSum) + dfs(node.right,currSum)
        return dfs(root,0)
        