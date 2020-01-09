# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        if head.next == None:
            return True
        count = 0
        t_head = head
        while t_head.next != None:
            t_head.next.__setattr__('pre', t_head)
            t_head = t_head.next
            count = count +1
        for i in range(0,(count+1)//2):
            print(t_head.val, head.val)
            if t_head.val == head.val:
                t_head = t_head.pre
                head = head.next
            else:
                return False
        return True
        

if __name__ == '__main__':
    input_lists = [[1,2],[1,2,2,1], [1,2,3,4,4,3,2,1], [0,0,0,0,0]]
    input_node_list = [ListNode(1)]
    for input_list in input_lists:
        input_node = ListNode(input_list[0])
        temp = input_node
        for i in input_list[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        input_node_list.append(input_node)

    s = Solution()
    for index in range(len(input_node_list)):
        print("Input Node {}".format(index))
        print(s.isPalindrome(input_node_list[index]))

