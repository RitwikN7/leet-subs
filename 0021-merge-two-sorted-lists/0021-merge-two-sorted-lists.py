# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        copy = res
        
        while list1 and list2:
            v1 = list1.val
            v2 = list2.val
            
            if v1 <= v2:
                res.next = ListNode(v1)
                list1 = list1.next
            else:
                res.next = ListNode(v2)
                list2 = list2.next
                
            res = res.next
            
        if list1:
            res.next = list1
            
        if list2:
            res.next = list2
            
        return copy.next
                
            
        
            