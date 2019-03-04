    
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class solution:  
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = l1
        j = l2
        head = ListNode(0)
        h = head
        while i and j:
            if i.val < j.val:
                h.next = i
                i = i.next
                # print(h.val)
            else:
                h.next = j
                j = j.next
                # print(h.val)
            h= h.next
        if i:
            h.next = i
        else:
            h.next = j
        
        return head.next


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)

    solution = solution()
    head3 = solution.mergeTwoLists(head1,head2)

    while head3:
        print(head3.val)
        head3 = head3.next
