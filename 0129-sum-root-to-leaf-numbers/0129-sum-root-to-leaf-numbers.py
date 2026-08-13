class Solution:
    def sumNumbers(self, root):
        def dfs(node, num):
            if not node:
                return 0

            num = num * 10 + node.val

            # Leaf node
            if not node.left and not node.right:
                return num

            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)