class Solution(object):
    def middleNode(self, head):
        pivot = head
        end = pivot
        try:
            while True:
                end = end.next.next
                pivot = pivot.next
        except:
            return pivot