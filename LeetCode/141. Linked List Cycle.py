class Solution(object):
    def hasCycle(self, head):
        res = set()
        while head:
            if head in res: return True
            else: res.add(head)
            head = head.next
        return False
        