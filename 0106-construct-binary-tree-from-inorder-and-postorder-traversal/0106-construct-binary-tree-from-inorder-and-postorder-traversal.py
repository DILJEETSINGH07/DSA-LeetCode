# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        index = {v: i for i, v in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def build(left, right):
            nonlocal post_idx

            if left > right:
                return None

            root_val = postorder[post_idx]
            post_idx -= 1

            root = TreeNode(root_val)

            mid = index[root_val]

            # Build right first
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)