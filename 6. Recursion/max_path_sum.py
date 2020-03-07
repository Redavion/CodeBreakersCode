# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxPathHelper(root):
            nonlocal maxSum
            if root is None:
                return 0

            leftMaxSum = max(maxPathHelper(root.left), 0)
            rightMaxSum = max(maxPathHelper(root.right), 0)
            #returns maxSum IF this node is the highest point
            maxSumIfHighestNode = max(leftMaxSum +root.val+ rightMaxSum, maxSum)

            maxSum = max(maxSum, maxSumIfHighestNode)

            #we can do maxsum of left and maxsum of right but not both
            return root.val + max(leftMaxSum, rightMaxSum)
        
        #if we do both we are declaring a new path
        maxSum = float('-inf')
        return max(maxPathHelper(root), maxSum)