class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
            
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        else:   
            root.left = self.insertIntoBST(root.left,val)
        return root
