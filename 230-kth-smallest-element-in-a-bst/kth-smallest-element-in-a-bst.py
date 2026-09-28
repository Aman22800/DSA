class Solution:
    def kthSmallest(self, root, k):
        # Store the inorder traversal of the BST
        arr = []

        def inorder(node):
            # Base case: if node doesn't exist, stop
            if not node:
                return

            # Visit the left subtree first
            inorder(node.left)

            # Visit the current node
            arr.append(node.val)

            # Visit the right subtree
            inorder(node.right)

        # Perform inorder traversal
        # For a BST, this gives values in sorted order
        inorder(root)

        # Since arrays are 0-indexed,
        # kth smallest element is at index k-1
        return arr[k - 1]