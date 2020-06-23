# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) : 
        self.count = 0
    def search(self,root):
        if(root==None) : return 
        self.count+=1
        self.search(root.left)
        self.search(root.right)
    def countNodes(self, root: TreeNode) -> int:
        self.search(root)
        return self.count
        