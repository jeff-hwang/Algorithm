class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # TreeNode 가 존재하지 않을 때 True
        if not root:
            return True

        # root의 left 가 존재하고 root의 val 과 root의 left의 val 값이 다르면
        # return False
        if root.left and root.val != root.left.val:
            return False

        # root의 right 가 존재하고 root의 val과 root의 right의 val 값이 다르면
        # return False
        if root.right and root.val != root.right.val:
            return False

        # root의 left와 right의 val이 root의 val 과 같다면
        # left right를 완전 탐색하여 True 이면 True
        # False 이면 return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
