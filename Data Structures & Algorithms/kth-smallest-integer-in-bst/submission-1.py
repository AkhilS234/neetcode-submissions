# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, node: TreeNode, result: list[str]):

        if not node:
            return 
        self.inOrder(node.left, result)
        result.append(node.val)
        self.inOrder(node.right, result)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.inOrder(root, result)
        return result[k-1]

# Runtime: O(n) all nodes are processed once
# Space: O(n) array data structure is created with n elements, the same
#. as the number of nodes 

        