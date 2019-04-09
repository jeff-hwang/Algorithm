
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def postorder(self, root):
        lst = []
        if not root:
            return []

        if not root.children:
            return [root.val]

        for i in root.children:
            lst += self.postorder(i)

        lst += [root.val]
        return lst


if __name__ == "__main__":
    node = Node()
    sl = Solution().postorder(node)
