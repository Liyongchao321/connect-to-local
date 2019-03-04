    
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class solution:  
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = []
        count = 0
        temp = head
        while temp:
            node.append(temp)
            count = count+1
            temp = temp.next
        node.append(None)
        if count != n:
            prenode = node[count-n-1]
            postnode = node[count-n+1]
            prenode.next = postnode
            return head
        if count == n:
            return head.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = solution()
    head2 = solution.removeNthFromEnd(head, 5)

    while head2:
        print(head2.val)
        head2 = head2.next
