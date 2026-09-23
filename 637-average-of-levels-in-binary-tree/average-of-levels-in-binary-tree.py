# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:

        # If tree is empty
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:

            # Number of nodes in current level
            level_size = len(queue)

            # Sum of values in current level
            total = 0

            for i in range(level_size):

                # Get current node
                node = queue.popleft()

                # Add node value to total
                total += node.val

                # Add children for next level
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Average = sum / number of nodes
            result.append(total / level_size)

        return result