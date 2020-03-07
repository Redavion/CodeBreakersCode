# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isValidHelper(node, minimum, maximum):
	if node is None:
		return True
	if node.value >= maximum or node.value < minimum:
		return False
	return isValidHelper(node.right, node.value, maximum) and isValidHelper(node.left, minimum, node.value)

def validateBst(tree):
    # Write your code here.
	return isValidHelper(tree, float("-inf"), float("inf"))
