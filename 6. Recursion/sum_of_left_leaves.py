# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        if root.left is None:
            return self.sumOfLeftLeaves(root.right)
	
        return root.left.val + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
