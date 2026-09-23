# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root:
            return []
        
        result=[]
        queue=deque([root])
        temp=[]

        while queue:
            level_size=len(queue)

            for i in range(level_size):
                node=queue.popleft()
                temp.append(node.val)
                #print(temp)

                if i==level_size-1:
                    result.append(sum(temp)/level_size)
                    temp=[]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
        