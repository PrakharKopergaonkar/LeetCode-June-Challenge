# Question 26: Sum Root to Leaf Numbers 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0
    
    def count(self,root,string):
        if(root.left == None and root.right == None):
            self.sum+=int(string+str(root.val))
            return
        if(root.left!=None):
            self.count(root.left,string+str(root.val))
        if(root.right!=None):
            self.count(root.right,string+str(root.val))
            
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None) : return 0
        else:
            self.count(root,"")
            return self.sum
 