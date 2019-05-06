# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        resNode = None
        
        #res = sum([v*(10**i) for i, v in enumerate(li1)]) + sum([ v*(10**i) for i, v in enumerate(li2)])
        res = self.makedList(l1)+self.makedList(l2)
        for i in range(1, len(str(res))+1):
            cache = res%(10**i)
            if resNode == None:
                resNode = ListNode(cache//10**(i-1))
                continue
            self.addLinkedList(resNode, cache//10**(i-1))
            
        return resNode
    '''
    def makeList(self, li, lkd):
        while lkd !=None:
            li.append(lkd.val)
            lkd = lkd.next
    '''
    def makedList(self, li):
        cnt, res = 0, 0
        while li != None:
            res += (li.val * (10**cnt))
            cnt+=1
            li=li.next
        return res
            
        
    
    def addLinkedList(self, li, val):
        if li.next!=None:
            self.addLinkedList(li.next, val)
        else:
            li.next = ListNode(val)
        return li
            
            
                    