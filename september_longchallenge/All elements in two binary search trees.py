# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr=[]
        def inorderTraversal(root):
            if root:
                inorderTraversal(root.left)
                arr.append(root.val)
                inorderTraversal(root.right)
        inorderTraversal(root1)
        inorderTraversal(root2)
        arr.sort()
        return arr
