# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        res = None
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            res = ListNode(l1.val)
            l1 = l1.next
        else :
            res = ListNode(l2.val)
            l2 = l2.next
            
        while True:
            try:
                if l1.val <= l2.val:
                    self.addNext(res, l1.val)
                    l1 = l1.next
                else :
                    self.addNext(res, l2.val)
                    l2 = l2.next
            except:
                if l1!=None:
                    self.addNext(res, l1.val)
                    l1 = l1.next
                    continue
                    
                if l2!=None:
                    self.addNext(res, l2.val)
                    l2 = l2.next
                    continue
                break 
        return res
                
                
    def addNext(self, temp, val):
        if temp.next != None:
            self.addNext(temp.next, val)
            return
        temp.next=ListNode(val)