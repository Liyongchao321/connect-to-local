# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        copy_tree = TreeNode(root.val)
        self.reverse_copy(root, copy_tree)
        res = [True]
        self.compare_two_tree(root, copy_tree, res)
        return res[0]

    
    def in_order_to_list(self, root, res_list):
        if root != None:
            if root.left != None:
                self.in_order_to_list(root.left, res_list)
            elif root.right != None:
                res_list.append(None)
            res_list.append(root.val)
            if root.right != None:
                self.in_order_to_list(root.right, res_list)
            elif root.left != None:
                res_list.append(None)
    
    def reverse_copy(self, root, copy_root):
        if root != None:
            if root.left != None:
                print(root.left.val)
                copy_root.right = TreeNode(root.left.val)            
                self.reverse_copy(root.left, copy_root.right)
            if root.right != None:
                print(root.right.val)
                copy_root.left = TreeNode(root.right.val)
                self.reverse_copy(root.right, copy_root.left)
    
    def compare_two_tree(self, tree_1, tree_2, res):
        if tree_1 != None and tree_2 != None:
            if tree_1.val != tree_2.val:
                res[0] = False
            else:
                self.compare_two_tree(tree_1.left, tree_2.left, res)
                self.compare_two_tree(tree_1.right, tree_2.right, res)
        elif (tree_1 == None and tree_2 != None) or (tree_2 == None and tree_1 != None):
            res[0] = False

if __name__ == '__main__':
    tree_1 = TreeNode(2)
    tree_1.right = TreeNode(3)
    tree_1.left = TreeNode(1)

    tree_3 = TreeNode(2)
    tree_3.right = TreeNode(3)
    tree_3.left = TreeNode(1)

    tree_2 = TreeNode(2)
    tree_2.left = TreeNode(1)
    tree_2.right = TreeNode(4)
    tree_2.right.left = TreeNode(3)
    tree_2.right.right = TreeNode(6)

    tree_4 = TreeNode(2)
    tree_4.left = TreeNode(1)
    tree_4.right = TreeNode(3)
    tree_4.left.left = TreeNode(5)
    tree_4.right.right = TreeNode(6)

    tree_5 = TreeNode(1)
    tree_5.left = TreeNode(2)
    tree_5.right = TreeNode(2)
    tree_5.left.left = TreeNode(2)
    tree_5.right.left = TreeNode(2)
    
    tree_6 = TreeNode(1)
    tree_6.left = TreeNode(2)
    tree_6.right = TreeNode(2)
    tree_6.left.left = TreeNode(2)
    tree_6.right.left = TreeNode(2)

    s = Solution()
    res = s.isSymmetric(tree_5)
    print(res)

    # list_tree_4 = []
    # s = Solution()
    # s.in_order_to_list(tree_4, list_tree_4)
    # print(list_tree_4)

    # copy_tree = TreeNode(tree_4.val)
    # s.reverse_copy(tree_4, copy_tree)
    # copy_tree_list = []
    # s.in_order_to_list(copy_tree, copy_tree_list)
    # print(copy_tree_list)
    
    # res = [True]
    # s.compare_two_tree(tree_1, tree_3, res)
    # s.compare_two_tree(tree_5, tree_6, res)
    # # s.compare_two_tree(tree_4, copy_tree, res)
    # print(res)


    