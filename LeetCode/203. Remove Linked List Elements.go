package main

func removeElements(head *ListNode, val int) *ListNode {
	if head == nil {
		return head
	} // head가 null 이면 return head
	head.Next = removeElements(head.Next, val) // removeElements를 재귀호출하며 탐색
	if head.Val == val {
		return head.Next
	} else {
		return head
	} // head의 값이 val과 같다면 다음 노드를 리턴
}
