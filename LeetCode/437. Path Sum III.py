class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def leftAppend(self, val):
        self.left = TreeNode(val)
    
    def righAppend(self, val):
        self.right = TreeNode(val)
        
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        

if __name__ == "__main__":
    sl = Solution()
    print(pathSum)
        