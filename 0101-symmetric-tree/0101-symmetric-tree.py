# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        def mirror(left, right):
            # Both are empty
            if not left and not right:
                return True

            # One is empty
            if not left or not right:
                return False

            # Values must match
            if left.val != right.val:
                return False

            # Compare opposite children
            return (mirror(left.left, right.right) and
                    mirror(left.right, right.left))

        return mirror(root.left, root.right)