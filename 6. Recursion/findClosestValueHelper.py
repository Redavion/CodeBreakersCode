def findClosestValueHelper(root, target, closestVal):
	if root is None:
		return closestVal
	if abs(root.value - target) < abs(closestVal - target):
		closestVal = root.value
	if root.value < target:
		return findClosestValueHelper(root.right, target, closestVal)
	return findClosestValueHelper(root.left, target, closestVal)
	
def findClosestValueInBst(tree, target):
    # Write your code here.
	closestVal = float("inf")
	return findClosestValueHelper(tree, target, closestVal)
