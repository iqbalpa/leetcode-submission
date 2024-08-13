# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head = None
        node1 = list1
        node2 = list2
        temp = None
        current = None
        while node1 != None and node2 != None:
            if node1.val < node2.val:
                temp = node1
                node1 = node1.next
            else:
                temp = node2
                node2 = node2.next
            if head is None:
                head = temp
                current = head
            else: 
                current.next = temp
                current = temp
        if node1 is None:
            current.next = node2
        if node2 is None:
            current.next = node1
        return head
