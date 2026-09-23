# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, h: Optional[ListNode]) -> None:
        s = h
        f = h.next

        while f and f.next:
            s = s.next
            f = f.next
            f = f.next
        
        sec = s.next
        s.next = None
        prev = None
        
        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp
        
        first = h
        sec = prev
        while first and sec:
            tmp1, tmp2 = first.next, sec.next
            first.next = sec
            sec = tmp2
            first.next.next = tmp1
            first = first.next.next
