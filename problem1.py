# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    stack = []
    
    def __init__(self, root: Optional[TreeNode]):
        self.dfs(root)
        
    # time: O(n)
    # space: O(n)
    def next(self) -> int:
        node = self.stack.pop()
        self.dfs(node.right)
        return node.val
    
    # time: O(1)
    def hasNext(self) -> bool:
        return len(self.stack)!=0

    # time: O(n)  
    def dfs(self,root):
        while root:
            self.stack.append(root)
            root=root.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()