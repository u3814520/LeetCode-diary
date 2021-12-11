class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def findMin(n1,n2):
            if n1 == None :
                return n2
            if n2 == None :
                return n1
            if n1.val < n2.val :
                n1.next = findMin(n1.next , n2)
                return n1
            else:
                n2.next = findMin(n1,n2.next)
                return n2
        return findMin(l1,l2)
