class Solution(object):
    def removeElements(self, head, val):
        if not head: return head
        head.next = self.removeElements(head.next,val)
        return head.next if head.val==val else head
            
            
        
        
        