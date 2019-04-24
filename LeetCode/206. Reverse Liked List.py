class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # LinkedList currentData
        curData = head
        
        # 반복문 후 가공된 데이터
        preData = None
        
        # 현재 node 가 None 일 때까지 반복
        while curData :
            # swap val - 현재 node의 next 값을 백업
            temp = curData.next
            # 현재 노드의 next 값을 = preData 로 저장
            curData.next = preData
            # preData 에 현재 노드를 대입
            preData = curData
            # 현재 노드에 백업해놓은 Node 대입
            curData = temp
        
        # reversed 된 Linked List return
        return preData
