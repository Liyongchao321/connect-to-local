# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if root == None:
    #         return True
    #     t_list = []
    #     self.mid_order(root, t_list)
    #     for i in range(1, len(t_list)):
    #         if t_list[i-1] >= t_list[i]:
    #             return False
    #     return True

    # def mid_order(self, root, res):
    #     if root != None:
    #         print('val',root.val)
    #         if root.left != None:
    #             print("get in left", root.left.val)
    #             self.mid_order(root.left, res)
                
    #         res.append(root.val)
    #         if root.right != None:
    #             print('get in right', root.right.val)
    #             self.mid_order(root.right, res)

    def mid_order(self, root):
        if root != None:
            print('val',root.val)
            if root.left != None:
                print("get in left", root.left.val)
                for i in self.mid_order(root.left):
                    yield i 
            print('return value:',root.val)           
            yield root
            if root.right != None:
                print('get in right', root.right.val)
                for i in self.mid_order(root.right):
                    yield i
  
    def isValidBST(self, root):
        res = self.mid_order(root)
        try:
            temp = -1
            while True:
                temp2 = next(res).val 
                print('iter move on')
                if temp >= temp2:
                    return False
                else:
                    temp = temp2
        except StopIteration as e:
            print('stop')
        return True



if __name__ == '__main__':
    tree_1 = TreeNode(2)
    tree_1.right = TreeNode(3)
    tree_1.left = TreeNode(1)

    tree_2 = TreeNode(2)
    tree_2.left = TreeNode(1)
    tree_2.right = TreeNode(4)
    tree_2.right.left = TreeNode(3)
    tree_2.right.right = TreeNode(6)

    s = Solution()
    # res = s.mid_order(tree_1)
    # print(next(res).val)
    # print(next(res).val)
    # print(next(res).val)
    # print(next(res).val)
    # try:
    #     while True:
    #         x = next(res).val
    #         print(x)
    # except StopIteration as e:
    #     print('ahah')
    
    # print(s.isValidBST(tree_1))
    print(s.isValidBST(tree_2))

    


